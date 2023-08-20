from shlex import join
import matplotlib.pyplot as plt
import numpy as np
import json
import utils
import os
import pandas as pd
log_path = "/mnt/a/OneDrive/MScRobotics/Dissertation2022/codes/experiment_results/agent_number vs frame_length/v3/FrameLen60_60agentsAug192128ReLen60.log"
log_parent_path = "/mnt/a/OneDrive/MScRobotics/Dissertation2022/codes/experiment_results/agent_number vs frame_length/v3"


def average_performance(params1, params2, performance):
    # Create a DataFrame from the input arrays
    df = pd.DataFrame({'param1': params1, 'param2': params2, 'performance': performance})
    
    # Group by the parameters and calculate the mean performance for each group
    grouped = df.groupby(['param1', 'param2']).mean().reset_index()
    
    # Return the unique parameters and averaged performance as separate arrays
    return grouped['param1'].values, grouped['param2'].values, grouped['performance'].values


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
        agent_total = data["num_nodes"]
        frame_length = data["num_slots"]
        frames = data["history"]
        required_length = data["required_length"]

        print("帧长度："+str(frame_length))
        print("节点数："+str(agent_total))
        print("要求的计划长度："+str(required_length))

        starts, goals, optimal_dists = scene_reader(scene_path)

        # 用帧重构各节点轨迹
        traces = {}  # 格式： 节点名：[[位置]]
        for key, values in frames.items():
            # key = 时间，value = [ [节点id（int），[x,y] ] ]
            for agents in values:
                agent_id = agents[0]  # 节点名
                position = agents[1]  # [x,y]
                # 在后面加上新位置
                if agent_id in traces:
                    traces[agent_id].append(position)
                else:
                    traces[agent_id] = [position]

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
        avg_real_vs_optimal = sum/agent_total
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

        # 3. 平均完成时间
        avg_finish_time = 0
        # 对于每个agent，找出其在网络中存在的最后一刻
        agents_ended = set()
        found_agents = 0
        for time, frame in reversed(frames.items()):
            for agent in frame:
                if agent[0] not in agents_ended:
                    agents_ended.add(agent[0])
                    avg_finish_time+=int(time)
                    found_agents+=1
        if found_agents!=agent_total: print("FATAL!")
        print("全部耗时：%d"%avg_finish_time)
        
        avg_finish_time=avg_finish_time/agent_total
        print("平均抵达终点时间：%f"%avg_finish_time)

        # 4. 加入网络的平均耗时
        # 先看出每人的耗时
        join_time = {}
        agents_visited = set()
        for time, frame in frames.items():
            for agent in frame:
                agent_id = agent[0]
                if agent_id not in agents_visited:
                    agents_visited.add(agent_id)
                    join_time[agent_id] = int(time)
        times = list(join_time.values())
        sum_time = 0
        for time in times:
            sum_time += time
        avg_join_spent_time = sum_time/len(times)
        print("有%d/%d个节点成功入网，每个节点加入网络的平均耗时是：%d" %
              (len(times), agent_total, avg_join_spent_time))
        
        # 5. 实际路径总长度vs最优路径总长度
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

        return agent_total, frame_length, avg_real_vs_optimal, finish_time, avg_finish_time, avg_join_spent_time, sum_actural_vs_optimal, required_length


def main():
    logs = traverse_directory(log_parent_path)



    # 读取两组实验数据
    # horizon = 30
    horizon_30_parent_path = '/mnt/a/OneDrive/MScRobotics/Dissertation2022/codes/experiment_results/performance_vs_requiedplanlength/horizon=30'
    horizon_30_logs = traverse_directory(horizon_30_parent_path)

    agent_totals_30            = []
    frame_lengths_30           = []
    avg_real_vs_optimals_30    = []
    finish_times_30             = []
    avg_finish_times_30        = []
    avg_join_spent_times_30 = []
    sum_actural_vs_optimals_30  = []
    required_lengths_30 = []

    for log in horizon_30_logs:
        a,b,c,d,e,f,g,h = log_reader(log)
        agent_totals_30.append(a)
        frame_lengths_30.append(b)
        avg_real_vs_optimals_30.append(c)
        finish_times_30.append(d)
        avg_finish_times_30.append(e)
        avg_join_spent_times_30.append(f)
        sum_actural_vs_optimals_30.append(g)
        required_lengths_30.append(h)

    # horizon = 60

    horizon_60_parent_path = '/mnt/a/OneDrive/MScRobotics/Dissertation2022/codes/experiment_results/performance_vs_requiedplanlength/horizon=60'

    horizon_60_logs = traverse_directory(horizon_60_parent_path)

    agent_totals_60            = []
    frame_lengths_60           = []
    avg_real_vs_optimals_60    = []
    finish_times_60             = []
    avg_finish_times_60        = []
    sum_actural_vs_optimals_60  = []
    avg_join_spent_times_60 = []
    required_lengths_60 = []

    for log in horizon_60_logs:
        a,b,c,d,e,f,g,h = log_reader(log)
        agent_totals_60.append(a)
        frame_lengths_60.append(b)
        avg_real_vs_optimals_60.append(c)
        finish_times_60.append(d)
        avg_finish_times_60.append(e)
        avg_join_spent_times_60.append(f)
        sum_actural_vs_optimals_60.append(g)
        required_lengths_60.append(h)

    # 生成上下两列，各自是路径效率的图


    # 注意坐标轴度量对齐

    # 画图
    fig = plt.figure(figsize=(12,12))
    
    # horizon = 30 real/optimal
    ax1 = fig.add_subplot(2, 2, 1, projection='3d')
    ax1.scatter(frame_lengths_30, required_lengths_30, sum_actural_vs_optimals_30, c=sum_actural_vs_optimals_30, cmap='viridis', marker='o')
    ax1.plot_trisurf(frame_lengths_30, required_lengths_30, sum_actural_vs_optimals_30, cmap='viridis', alpha=0.5)
    ax1.set_title('total path efficiency ratio (horizon=30)',y=0.92,fontsize=12)

    ax1.set_ylabel("plan length limit",fontsize=12)
    ax1.set_xlabel("frame length = agent number",fontsize=12)
    ax1.set_zlabel("total path efficiency",fontsize=12)   
    ax1.set_zlim(1.0,2.0)
    ax1.view_init(elev=10, azim=-146)

    # horizon = 30 avg real/optimal
    ax2 = fig.add_subplot(2, 2, 2, projection='3d')
    ax2.scatter(frame_lengths_30, required_lengths_30, avg_real_vs_optimals_30, c=sum_actural_vs_optimals_30, cmap='viridis', marker='o')
    ax2.plot_trisurf(frame_lengths_30, required_lengths_30, avg_real_vs_optimals_30, cmap='viridis', alpha=0.5)
    ax2.set_title('average path efficiency ratio (horizon = 30)',y=0.92)

    ax2.set_ylabel("plan length limit",fontsize = 12)
    ax2.set_xlabel("frame length = agent number",fontsize=12)
    ax2.set_zlabel("average path efficiency",fontsize=12)   
    ax2.set_zlim(1.0,2.0)
    ax2.view_init(elev=10, azim=-146)





    # horizon = 60 real/optimal
    ax3 = fig.add_subplot(2, 2, 3, projection='3d')
    ax3.scatter(frame_lengths_60, required_lengths_60, sum_actural_vs_optimals_60, c=sum_actural_vs_optimals_60, cmap='viridis', marker='o')
    ax3.plot_trisurf(frame_lengths_60, required_lengths_60, sum_actural_vs_optimals_60, cmap='viridis', alpha=0.5)
    ax3.set_title('total path efficiency ratio (horizon = 60)',y=0.92,fontsize=12)
    ax3.set_ylabel("plan length limit",fontsize=12)
    ax3.set_xlabel("frame length = agent number",fontsize=12)
    ax3.set_zlabel("total path efficiency",fontsize=12)   
    ax3.set_zlim(1.0,2.0)
    ax3.view_init(elev=10, azim=-146)

    # horizon = 60 avg real/optimal
    ax4 = fig.add_subplot(2, 2, 4, projection='3d')
    ax4.scatter(frame_lengths_60, required_lengths_60, avg_real_vs_optimals_60, c=sum_actural_vs_optimals_60, cmap='viridis', marker='o')
    ax4.plot_trisurf(frame_lengths_60, required_lengths_60, avg_real_vs_optimals_60, cmap='viridis', alpha=0.5)
    ax4.set_title('average path efficiency ratio (horizon = 60)',y=0.92,fontsize=12)
    ax4.set_ylabel("plan length limit",fontsize=12)
    ax4.set_xlabel("frame length = agent number",fontsize=12)
    ax4.set_zlabel("average path efficiency",fontsize=12)   
    ax4.set_zlim(1.0,2.0)
    ax4.view_init(elev=10, azim=-146)

    plt.tight_layout()
    plt.show()



if __name__ == "__main__":
    main()
