import json
from turtle import pos
import utils
log_path = "/mnt/a/OneDrive/MScRobotics/Dissertation2022/codes/experiment_results/log1.log"

def main():
    with open(log_path,"r") as log:
        data = json.load(log)

        scene_path = data["scene_path"]
        map_path = data["map_path"]
        map_size = data["map_size"]
        frames = data["history"]

        node_number, map_path_, map_size_, starts, goals = utils.scene_reader(scene_path)

        print(scene_path)
        print(map_path)
        print(map_path_)

        
        # 判断地图对不对得上
        assert map_path_ == map_path

        # 用帧重构各节点轨迹
        traces = {} # 格式： 节点名：[[位置]]
        for key,values in frames.items():
            # key = 时间，value = [ [str(节点名)，[x,y] ] ]
            for nodes in values:
                node_id = nodes[0]  # 节点名
                position = nodes[1] # [x,y]
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
        starts_goals = {}
        for key, value in traces.items():
            node_id = key
            actural_start = value[0]
            
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