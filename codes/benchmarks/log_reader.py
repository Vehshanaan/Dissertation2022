import matplotlib.pyplot as plt
import numpy as np
import json
import utils
import os
log_path = "/mnt/a/OneDrive/MScRobotics/Dissertation2022/codes/experiment_results/Berlin_1_256.png/FrameLen10_20NodesJul181544.log"
log_parent_path = "/mnt/a/OneDrive/MScRobotics/Dissertation2022/codes/experiment_results/Performance_vs_Required_Plan_Length"

def traverse_directory(directory_path):
    result = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if os.path.splitext(file)[1] == ".log":
                file_path = os.path.join(root, file)
                result.append(file_path)
    return result


def scene_reader(scene_path, min_dist=-1):
    '''
    读入标准scene文件，返回起点和终点数组

    Args:
        scene_path (str, optional): scene文件的路径. 默认值在launch.py中.

        min_dist (int): 起点和终点之间的最小距离，小于这个距离的将被滤除

    Returns:

        starts [(x,y)]: 起点的坐标

        goals [(x,y)]: 终点的坐标
    '''
    starts = []
    goals = []
    optimal_dists = []
    with open(scene_path, "r") as scene:
        for line in scene:
            words = line.strip().split(" ")
            if len(words) == 2:
                continue  # 过滤掉开头的version空格1
            words = words[0].strip().split("\t")
            # 第5，6个元素是起点横纵坐标
            start = (int(words[4]), int(words[5]))
            # 第7，8个元素是终点横纵坐标
            goal = (int(words[6]), int(words[7]))
            # 最后一个元素是最优距离
            optimal_dist = float(words[-1])
            optimal_dists.append(optimal_dist)
            if optimal_dist < min_dist:
                continue  # 如果最优距离小于阈值：跳过，不读入这组起终点
            starts.append(start)
            goals.append(goal)
    return starts, goals, optimal_dists


def log_reader(log_path):

    with open(log_path, "r") as log:
        data = json.load(log)

        scene_path = data["scene_path"]
        #print(scene_path)
        map_path = data["map_path"]
        map_size = data["map_size"]
        node_total = data["num_nodes"]
        frame_length = data["num_slots"]
        frames = data["history"]
        required_length = data["required_length"]

        print("帧长度："+str(frame_length))
        print("节点数："+str(node_total))
        print("要求的计划长度："+str(required_length))

        starts, goals, optimal_dists = scene_reader(scene_path)

        # 用帧重构各节点轨迹
        traces = {}  # 格式： 节点名：[[位置]]
        for key, values in frames.items():
            # key = 时间，value = [ [节点id（int），[x,y] ] ]
            for nodes in values:
                node_id = nodes[0]  # 节点名
                position = nodes[1]  # [x,y]
                # 在后面加上新位置
                if node_id in traces:
                    traces[node_id].append(position)
                else:
                    traces[node_id] = [position]

        # 指标：

        # 1. 平均 最优路径长度/实际路径长度
        # sum (路径/最优)
        sum = 0
        for trace in traces.values():
            start = trace[0]
            index = starts.index(tuple(start))
            goal = goals[index]  # 对应的终点
            optimal = optimal_dists[index]  # 最优距离
            sum += len(trace)/optimal
        avg_real_vs_optimal = sum/node_total
        print("实际路径长度/最优路径总长度："+str(avg_real_vs_optimal))

        

        # 2. 整体完成时间
        # 寻找最后一次空的前一个
        time = list(frames.keys())
        frame = list(frames.values())
        i = len(time)-1
        prev = True
        finish_time = -1
        while i >= 0:
            current = frame[i]  # 当前帧中节点们的位置
            if not prev and current:  # 如果后一帧空而此帧不空：就是你了
                finish_time = int(time[i])
            prev = current
            i -= 1
        if finish_time != -1:
            print("全部抵达终点时间：%d步。" % finish_time)
        else:
            print("没有全部到达终点")
        # 3. 加入网络的平均耗时
        # 先看出每人的耗时
        join_time = {}
        nodes_visited = set()
        for time, frame in frames.items():
            for node in frame:
                node_id = node[0]
                if node_id not in nodes_visited:
                    nodes_visited.add(node_id)
                    join_time[node_id] = int(time)
        times = list(join_time.values())
        sum_time = 0
        for time in times:
            sum_time += time
        avg_join_spent_time = sum_time/len(times)
        print("有%d/%d个节点成功入网，每个节点加入网络的平均耗时是：%d" %
              (len(times), node_total, avg_join_spent_time))
        
        # 4. 实际路径总长度vs最优路径总长度
        sum_actural = 0
        sum_optimal = 0
        for trace in traces.values():
            start = trace[0] # 路径开头就是起点
            index = starts.index(tuple(start)) # 根据起点获知他是谁
            goal = goals[index] # 根据他是谁获知其终点
            optimal = optimal_dists[index] #  最优距离
            sum_actural+=len(trace)
            sum_optimal+=optimal
        sum_actural_vs_optimal = sum_actural/sum_optimal # 实际路径总长度vs最优总长度
        print("总实际路径长度/最优路径长度：%f"%sum_actural_vs_optimal)

        return node_total, frame_length, avg_real_vs_optimal, finish_time, avg_join_spent_time, sum_actural_vs_optimal


def main():
    log_files = traverse_directory(log_parent_path)
    

    node_total = []
    frame_length = []
    real_vs_optimal_avg=[]
    finishtime = []
    join_spent_time = []
    real_vs_optimal_sum = []

    for log in log_files:
        print(log)
        a,b,c,d,e,f= log_reader(log)
        node_total.append(a)
        frame_length.append(b)
        real_vs_optimal_avg.append(c)
        finishtime.append(d)
        join_spent_time.append(e)
        real_vs_optimal_sum.append(f)




if __name__ == "__main__":
    main()
