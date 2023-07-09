import json
from shlex import join
from turtle import pos
import utils
log_path = "/mnt/a/OneDrive/MScRobotics/Dissertation2022/codes/experiment_results/Berlin_0_256.png/NodeNum50(80, 80)1250.log"
import utils

def main():
    with open(log_path, "r") as log:
        data = json.load(log)

        scene_path = data["scene_path"]
        map_path = data["map_path"]
        map_size = data["map_size"]
        frames = data["history"]
        network_status = data["joined_node_number"]

        node_number, map_path_, map_size_, starts, goals = utils.scene_reader(
            scene_path)

        print(scene_path)
        print(map_path)
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
        pure_trace = {} # node_id: [[位置]] 不包含起始的复读起点和终点的复读终点
        # 去尾
        for node_id,trace in traces.items():
            path = []
            start = starts_goals[node_id][0]
            goal = starts_goals[node_id][1]
            # 去尾
            for pos in trace: # 如果我==终点：从我掐掉
                path.append(pos)
                path.append(pos)
                if pos == goal: break
            # 掐头
            for i in range(len(path)):
                if path[i]==start and i+1<len(path) and path[i+1]!=start: # 如果自己=起点且后一个！=起点：从我把前面掐掉
                    path = path[i:-1]
                    break
    
            pure_trace[node_id] = path
            
                
        # makespan: 所有agent完成路径的最大时间
        makespan = [-1,-1] # 最长者id, makespan
        for node_id, trace in pure_trace.items():
            if len(trace)>makespan[1]:
                makespan[1] = len(trace)
                makespan[0] = node_id
        print("最慢的是%s, 其路径总长为%d（除去起点复读和终点复读，即舍去加入时间）"%(makespan[0],makespan[1]))
        #print("它的纯净路径看起来是这样的："+str(pure_trace[makespan[0]]))

        # 成功率：agent成功找到路径的几率
        success_nodes = []
        failed_nodes = []
        for node_id,value in pure_trace.items():
            if value[-1]==starts_goals[node_id][1]:
                success_nodes.append(node_id)


            else: 
                failed_nodes.append(node_id)

        print("共%d个节点，%d个成功到达终点，成功率为%d%%"%(node_number,len(success_nodes),len(success_nodes)/node_number*100))
        
        # flowtime: 所有agent完成路径的总时间
        flowtime = 0
        for trace in pure_trace.values():
            flowtime+=len(trace)
        print("所有节点的路径（舍去加入网络的时间）总长度为:%d"%flowtime)
        # 全部节点入网耗时
        joined_node_number_max = -1
        for time,value in network_status.items():
            if value>joined_node_number_max:joined_node_number_max = value
        print("入网（曾发送过计划的）节点：%d / %d"%(joined_node_number_max,node_number))        
        
        # 实际路径/最优路径比
        map = utils.map_load(map_path,map_size)

        # 计算最优路径
        optimal_paths = {}
        for node_id, value in starts_goals.items():
            start = value[0]
            goal = value[1]
            optimal_path = utils.find_path_optimal(map,start,goal)
            optimal_paths[node_id] = optimal_path
        
        # 统计最优路径versus实际路径长度的比 这里回来应该用单个节点的场景测试一下
        versus_optimal_rates = {}
        for node_id, trace in pure_trace.items():
            actural_length = len(trace)
            optimal_length = len(optimal_paths[node_id])
            if optimal_length == 0:continue
            rate = optimal_length/actural_length
            versus_optimal_rates[node_id] = rate

        avg_versus_optimal_rate = 0
        for rate in versus_optimal_rates.values():
            avg_versus_optimal_rate+=rate

        avg_versus_optimal_rate=avg_versus_optimal_rate/len(list(versus_optimal_rates.keys()))

        print("对于成功抵达终点的节点，它们的平均 理想路径/实际路径 比例为：%d%%" % (avg_versus_optimal_rate*100) )

        
        # 入网耗时检测
        


        ''' # 跳步检测：是否每一步仅移动一格
        for key, value in traces.items():
            for i in range(len(value)):
                if (i+1) < len(value):
                    if abs(value[i][0]-value[i+1][0])+abs(value[i][1]-value[i+1][1])>1:
                        print("跳步了")
                        print(value[i])
                        print(value[i+1])
                        print(value)
                        if i!=0:
                            print('甚至不是一开始跳步的')
        '''


if __name__ == "__main__":
    main()
