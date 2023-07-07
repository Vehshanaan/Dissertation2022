import json
from turtle import pos
import utils
log_path = "/mnt/a/OneDrive/MScRobotics/Dissertation2022/codes/experiment_results/log1.log"


def main():
    with open(log_path, "r") as log:
        data = json.load(log)

        scene_path = data["scene_path"]
        map_path = data["map_path"]
        map_size = data["map_size"]
        frames = data["history"]

        node_number, map_path_, map_size_, starts, goals = utils.scene_reader(
            scene_path)

        print(scene_path)
        print(map_path)
        print(map_path_)

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

        joined_nodes_num = len(traces.keys())
        print("入网节点数："+str(joined_nodes_num))
        unjoined_nodes_num = node_number - joined_nodes_num
        print("未入网节点数："+str(unjoined_nodes_num))

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
        
        # 50%节点入网耗时
        # 问题：算不算入网的耗时？

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
