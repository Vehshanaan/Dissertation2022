import json
from shlex import join
import stat
from turtle import pos
import utils
import os
log_path = "/mnt/a/OneDrive/MScRobotics/Dissertation2022/codes/experiment_results/Berlin_0_256.png/"
import utils
import numpy as np
import matplotlib.pyplot as plt

def traverse_directory(directory_path):
    result = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            result.append(file_path)
    return result



def log_reader(log_path):
    '''
    _summary_

    Args:
        log_path (str): 日志文件的路径

    Returns:
         - 以下路径若不说明则均不含起点和终点的复读长度

        node_number (int): 节点数目

        slowest_node_id (int): 拥有最长路径的节点的名字

        longest_path (int): 最长路径的长度

        success_rate (float): 成功到达终点的节点数

        flowtime (int): 所有路径的总长度

        avg_versus_optimal_rate (float): 最优路径（只有我一人在地图中运行）总长/实际路径总长

        all_join_time (int): 全部节点成功入网的耗时
    '''
    with open(log_path, "r") as log:
        data = json.load(log)

        scene_path = data["scene_path"]
        map_path = data["map_path"]
        map_size = data["map_size"]
        frames = data["history"]


        node_number, map_path_, map_size_, starts, goals = utils.scene_reader(
            scene_path)
        

        #print(scene_path)
        #print(map_path)
        if map_path!=map_path_:print("出情况了，从情景文件和日志文件读入的地图路径居然不一样")

        # 判断地图对不对得上
        assert map_path_ == map_path

        # 用帧重构各节点轨迹
        traces = {}  # 格式： 节点名：[[位置]]
        for key, values in frames.items():
            # key = 时间，value = [ [str(节点名)，[x,y] ] ]
            for nodes in values:
                node_id = nodes[0]  # 节点名
                position = nodes[1]  # [x,y]
                # 在后面加上新位置
                if node_id in traces:
                    traces[node_id].append(position)
                else:
                    traces[node_id] = [position]

        

        # 对每个节点，识别其起点终点
        starts_goals = {}  # node_id: start,goal
        for key, value in traces.items():
            node_id = key
            start = value[0]
            index = starts.index(start)
            goal = goals[index]
            starts_goals[node_id] = [start, goal]

        # 计算性能指标：
        # 先做出每个节点的路径（不包含起点处的重复和结尾处的重复）
        pure_traces = {} # node_id: [[位置]] 不包含起始的复读起点和终点的复读终点
        # 去尾
        for node_id,trace in traces.items():
            path = []
            start = starts_goals[node_id][0]
            goal = starts_goals[node_id][1]
            # 去尾
            for pos in trace: # 如果我==终点：从我掐掉
                path.append(pos)
                if pos == goal: 
                    path.append(goal)
                    break
            # 掐头
            for i in range(len(path)):
                if path[i]==start and i+1<len(path) and path[i+1]!=start: # 如果自己=起点且后一个！=起点：从我把前面掐掉
                    path = path[i:-1]
                    #path = [start]+path
                    break
            pure_traces[node_id] = path

                
        # makespan: 所有agent完成路径的最大时间
        makespan = [-1,-1] # 最长者id, makespan
        for node_id, trace in pure_traces.items():
            if len(trace)>makespan[1]:
                makespan[1] = len(trace)
                makespan[0] = node_id
        print("最慢的是%s, 其路径总长为%d（除去起点复读和终点复读，即舍去加入时间）"%(makespan[0],makespan[1]))
        #print("它的纯净路径看起来是这样的："+str(pure_trace[makespan[0]]))

        slowest_node_id = makespan[0]
        longest_path = makespan[1]

        # 成功率：agent成功找到路径的几率
        success_nodes = []
        failed_nodes = []
        for node_id,value in pure_traces.items():
            if value[-1]==starts_goals[node_id][1]:
                success_nodes.append(node_id)


            else: 
                failed_nodes.append(node_id)

        print("共%d个节点，%d个成功到达终点，成功率为%d%%"%(node_number,len(success_nodes),len(success_nodes)/node_number*100))
        
        success_rate = len(success_nodes)/node_number

        # flowtime: 所有agent完成路径的总时间
        flowtime = 0
        for trace in pure_traces.values():
            flowtime+=len(trace)
        print("所有节点的路径（舍去加入网络的时间）总长度为:%d"%flowtime)

        # 实际路径/最优路径比
        map = utils.map_load(map_path,map_size)

        # 计算最优路径
        optimal_traces = {}
        for node_id, value in starts_goals.items():
            start = value[0]
            goal = value[1]
            optimal_trace = [start]+utils.find_path_optimal(map,start,goal)
            optimal_traces[node_id] = optimal_trace

        
        # 统计最优路径versus实际路径长度的比 这里回来应该用单个节点的场景测试一下
        versus_optimal_rates = {}
        for node_id, trace in pure_traces.items():
            actural_length = len(trace)
            optimal_length = len(optimal_traces[node_id])
            if optimal_length == 0:continue
            rate = optimal_length/actural_length
            versus_optimal_rates[node_id] = rate

        avg_versus_optimal_rate = 0
        for rate in versus_optimal_rates.values():
            avg_versus_optimal_rate+=rate

        avg_versus_optimal_rate=avg_versus_optimal_rate/len(list(versus_optimal_rates.keys()))

        print("对于成功抵达终点的节点，它们的平均 理想路径/实际路径 比例为：%d%%" % (avg_versus_optimal_rate*100) )

        # 全部节点入网耗时
        all_join_time = -1
        # 全部节点的位置都不等于起点且全部起点存在时就说明全部入网且走过完整一轮了
        for time, frame in frames.items():
            if len(frame)!=node_number:continue# 如果存在节点个数不足：过\
           
            all_joined = True

            for positions in frame: # 如果有节点在自己的起点上：过
               node_id = positions[0]
               pos = positions[1]
               if pos == starts_goals[node_id][0]:
                   all_joined = False
            if all_joined: 
                all_join_time = int(time)
                break
                
        all_join_time -= node_number # 因为进入后再过一轮才能离开起点



        return node_number, slowest_node_id, longest_path, success_rate, flowtime, avg_versus_optimal_rate, all_join_time


if __name__ == "__main__":
    log_files = traverse_directory(log_path)

    node_num = []
    slowest_id = []
    longest_path = []
    success_rate = []
    flowtime = []
    avg_vs_optimal_rate = []
    all_join_time = []

    for log in log_files:  
        print(log)
        num, slowest, longest, success, flow, avg, all = log_reader(log)
        node_num.append(num)
        slowest_id.append(slowest)
        longest_path.append(longest)
        success_rate.append(success)
        flowtime.append(flow)
        avg_vs_optimal_rate.append(avg)
        all_join_time.append(all)
    
    # 画图
    # 转np数组
    node_num = np.array(node_num)
    slowest_id = np.array(slowest_id)
    longest_path=  np.array(longest_path)
    success_rate = np.array(success_rate)
    flowtime = np.array(flowtime)
    avg_vs_optimal_rate = np.array(avg_vs_optimal_rate)
    all_join_time = np.array(all_join_time)

    fig, axes = plt.subplots(3,2,figsize = (12,8))

    
    axes[0,0].bar(node_num,longest_path)
    axes[0,0].set_title("longest_path")

    axes[0,1].bar(node_num,success_rate)
    axes[0,1].set_title("success_rate")

    axes[1,0].bar(node_num,flowtime)
    axes[1,0].set_title("sum path length")

    axes[1,1].bar(node_num,flowtime/node_num)
    axes[1,1].set_title("path length avg node")

    axes[2,0].bar(node_num,avg_vs_optimal_rate)
    axes[2,0].set_title("avg optimal/actural")

    axes[2,1].bar(node_num,all_join_time/node_num)
    axes[2,1].set_title("avg join time spent")

    fig.tight_layout()
    plt.show()
    


    
