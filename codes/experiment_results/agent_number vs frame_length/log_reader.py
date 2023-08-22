import enum
from shlex import join
import matplotlib.pyplot as plt
import numpy as np
import json
import utils
import os
import pandas as pd
log_path = "/mnt/a/OneDrive/MScRobotics/Dissertation2022/codes/experiment_results/agent_number vs frame_length/node_number vs frame_length v2/FrameLen10_10NodesAug130910ReLen10.log"
log_parent_path1 = "/mnt/a/OneDrive/MScRobotics/Dissertation2022/codes/experiment_results/agent_number vs frame_length/node_number vs frame_length v2"
log_parent_path2 = "/mnt/a/OneDrive/MScRobotics/Dissertation2022/codes/experiment_results/agent_number vs frame_length/v3"


def average_performance(params1, params2, performance):
    # Create a DataFrame from the input arrays
    df = pd.DataFrame({'param1': params1, 'param2': params2,
                      'performance': performance})

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
        # print(scene_path)
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
                    avg_finish_time += int(time)
                    found_agents += 1
        if found_agents != agent_total:
            print("FATAL!")
        print("全部耗时：%d" % avg_finish_time)

        avg_finish_time = avg_finish_time/agent_total
        print("平均抵达终点时间：%f" % avg_finish_time)

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
            start = trace[0]  # 路径开头就是起点
            index = starts.index(tuple(start))  # 根据起点获知他是谁
            goal = goals[index]  # 根据他是谁获知其终点
            optimal = optimal_dists[index]  # 最优距离
            sum_actural += len(trace)
            sum_optimal += optimal
        sum_actural_vs_optimal = sum_actural/sum_optimal  # 实际路径总长度vs最优总长度
        print("总实际路径长度/最优路径长度：%f" % sum_actural_vs_optimal)

        # 6. 信道中同时存在之agent数
        agent_in_channel = {}
        for time, frame in frames.items():
            '''
            time = int(time)
            if time-frame_length < 0:
                continue
            agent_in_channel[time-frame_length] = len(frame)
            '''
            time = int(time)
            agent_in_channel[time] = len(frame)

        # 去除尾部无人区
        # 找到最后一个非零数据的索引
        last_nonzero_index = len(agent_in_channel) - 1
        for i, data in enumerate(reversed(agent_in_channel.values())):
            if data != 0:
                last_nonzero_index = len(agent_in_channel) - 1 - i
                break
            
        # 获取非零部分的时间和数据
        filtered_times = list(agent_in_channel.keys())[:last_nonzero_index + 1]
        filtered_data_values = list(agent_in_channel.values())[:last_nonzero_index + 1]
        
        agent_in_channel = {}
        for i in range(len(filtered_times)):
            agent_in_channel[filtered_times[i]] = filtered_data_values[i]
            
        # 尾部加一个0，方便看
        agent_in_channel[filtered_times[-1]+1] = 0
            


        return agent_total, frame_length, avg_real_vs_optimal, finish_time, avg_finish_time, avg_join_spent_time, sum_actural_vs_optimal, required_length, agent_in_channel


def main():

    # 读取两组实验日志路径
    logs1 = traverse_directory(log_parent_path1)
    logs2 = traverse_directory(log_parent_path2)

    # 读取两组实验数据
    # 第一组
    agent_total1 = []
    frame_length1 = []
    avg_real_vs_optimal1 = [] 
    finish_time1 = []
    avg_finish_time1 = [] 
    avg_join_spent_time1 = []
    sum_actural_vs_optimal1 = []
    required_length1 = []
    agent_in_channel1 = []
    for log in logs1:
        a,b,c,d,e,f,g,h,i = log_reader(log)
        agent_total1.append(a)
        frame_length1.append(b)
        avg_real_vs_optimal1.append(c)
        finish_time1.append(d)
        avg_finish_time1.append(e)
        avg_join_spent_time1.append(f)
        sum_actural_vs_optimal1.append(g)
        required_length1.append(h)
        agent_in_channel1.append(i)
    
    # 第二组
    agent_total2 = []
    frame_length2 = []
    avg_real_vs_optimal2 = [] 
    finish_time2 = []
    avg_finish_time2 = [] 
    avg_join_spent_time2 = []
    sum_actural_vs_optimal2 = []
    required_length2 = []
    agent_in_channel2 = []
    for log in logs2:
        a,b,c,d,e,f,g,h,i = log_reader(log)
        agent_total2.append(a)
        frame_length2.append(b)
        avg_real_vs_optimal2.append(c)
        finish_time2.append(d)
        avg_finish_time2.append(e)
        avg_join_spent_time2.append(f)
        sum_actural_vs_optimal2.append(g)
        required_length2.append(h)
        agent_in_channel2.append(i)  


    # 选一组channel中agent数量数据绘制

    '''
    # 选60agents的一组吧。
    indexs = []
    agent_number = 60
    for i in range(len(agent_total2)):
        if agent_total2[i] == agent_number:
            indexs.append(i)
    
    frame_length = []
    agent_total = []
    channel_usage = []
    for i in indexs:
        channel_usage.append(agent_in_channel2[i])
        frame_length.append(frame_length2[i])
        agent_total.append(agent_total2[i])
    
    # 画图
    plt.figure()

    color_cycle = plt.rcParams["axes.prop_cycle"].by_key()["color"]

    for i, result_dict in enumerate(channel_usage):
        times = list(result_dict.keys())
        values = np.array(list(result_dict.values()))
        values = values/agent_number*100
        color = color_cycle[i%len(color_cycle)+1]
        #plt.plot(times,values,color=color,label = "agent number = "+str(agent_total[i]))
        plt.plot(times,values,color=color,label = "frame length = " +str(frame_length[i]))
    plt.title("agent number = "+str(agent_number))
    plt.xlabel("time")
    plt.ylabel("% of agents in the channel")
    plt.legend()
    plt.grid()
    plt.ylim(-1,105)
    plt.xlim(-5,1000)
    plt.tight_layout()
    plt.show()
    '''
    
    
    
    # 信道使用率
    # 选60agents的一组吧。
    indexs = []
    agent_number = 50
    for i in range(len(agent_total2)):
        if agent_total2[i] == agent_number:
            indexs.append(i)
    
    frame_length = []
    agent_total = []
    channel_usage = []
    for i in indexs:
        channel_usage.append(agent_in_channel2[i])
        frame_length.append(frame_length2[i])
        agent_total.append(agent_total2[i])
    
    # 画图
    plt.figure()

    color_cycle = plt.rcParams["axes.prop_cycle"].by_key()["color"]

    for i, result_dict in enumerate(channel_usage):
        times = list(result_dict.keys())
        values = np.array(list(result_dict.values()))
        values = values/frame_length[i]*100
        color = color_cycle[i%len(color_cycle)]
        #plt.plot(times,values,color=color,label = "agent number = "+str(agent_total[i]))
        plt.plot(times,values,color=color,label = "frame length = " +str(frame_length[i]))
    plt.title("agent number = "+str(agent_number))
    plt.xlabel("time")
    plt.ylabel("channel usage (%)")
    plt.legend()
    plt.grid()
    plt.ylim(-1,105)
    plt.xlim(-5,1000)
    plt.tight_layout()
    plt.show()
    

    
    '''
    # 将其他的参数求平均
    agent_total = agent_total1+agent_total2
    frame_length = frame_length1+frame_length2
    avg_real_vs_optimal = avg_real_vs_optimal1+avg_real_vs_optimal2
    finish_time = finish_time1+finish_time2
    avg_finish_time = avg_finish_time1+avg_finish_time2
    avg_join_spent_time = avg_join_spent_time1+avg_join_spent_time2
    sum_actural_vs_optimal = sum_actural_vs_optimal1+sum_actural_vs_optimal2
    required_length = required_length1+required_length2
    
    _,_,avg_real_vs_optimal=average_performance(agent_total,frame_length,avg_real_vs_optimal)
    _,_,finish_time = average_performance(agent_total,frame_length,finish_time)
    _,_,avg_finish_time = average_performance(agent_total,frame_length,avg_finish_time)
    _,_,avg_join_spent_time = average_performance(agent_total,frame_length, avg_join_spent_time)
    agent_total,frame_length,sum_actural_vs_optimal = average_performance(agent_total,frame_length,sum_actural_vs_optimal)

    # 绘图
    fig = plt.figure(figsize=(12,12))
    
    # avg_finish_time
    x = agent_total
    y = frame_length
    z = avg_finish_time
    ax1 = fig.add_subplot(2,2, 1, projection='3d')
    ax1.scatter(x, y, z, c=z, cmap='viridis', marker='o')
    ax1.plot_trisurf(x,y,z, cmap='viridis', alpha=0.5)
    ax1.set_title('average agent arrival time',y=0.92,fontsize=12)
    ax1.set_xlabel("agent number",fontsize=12)
    ax1.set_ylabel("frame length",fontsize=12)
    ax1.set_zlabel("average agent arrival time",fontsize=12)   

    # 找到每个x值对应的z值最低的点的索引
    min_z_indices = []
    for xi in np.unique(x):
        mask = x == xi
        min_z_index = np.argmin(z[mask])
        min_z_indices.append(np.where(mask)[0][min_z_index])

    # 高亮每个x值对应的z值最低的点
    ax1.scatter(x[min_z_indices], y[min_z_indices], z[min_z_indices], c='r', marker='o',s=120, label='Min Z Points for each Agent Number')
    ax1.legend()
    ax1.view_init(elev=13, azim=-170)

    
    # finish time
    x = agent_total
    y = frame_length
    z = finish_time
    ax2 = fig.add_subplot(2, 2, 2, projection='3d')
    ax2.scatter(x, y, z, c=z, cmap='viridis', marker='o')
    ax2.plot_trisurf(x,y,z, cmap='viridis', alpha=0.5)
    ax2.set_title('final agent arrival time',y=0.92,fontsize=12)
    ax2.set_xlabel("agent number",fontsize=12)
    ax2.set_ylabel("frame length",fontsize=12)
    ax2.set_zlabel("final agent arrival time",fontsize=12)   

    # 找到每个x值对应的z值最低的点的索引
    min_z_indices = []
    for xi in np.unique(x):
        mask = x == xi
        min_z_index = np.argmin(z[mask])
        min_z_indices.append(np.where(mask)[0][min_z_index])

    # 高亮每个x值对应的z值最低的点
    ax2.scatter(x[min_z_indices], y[min_z_indices], z[min_z_indices], c='r', marker='o',s=120, label='Min Z Points for each Agent Number')
    ax2.legend()
    ax2.view_init(elev=13, azim=-170)

    # 平均入网耗时
    x = agent_total
    y = frame_length
    z = avg_join_spent_time
    ax3 = fig.add_subplot(2, 2, 3, projection='3d')
    ax3.scatter(x, y, z, c=z, cmap='viridis', marker='o')
    ax3.plot_trisurf(x,y,z, cmap='viridis', alpha=0.5)
    ax3.set_title("average network join time",y=0.92,fontsize=12)
    ax3.set_xlabel("agent number",fontsize=12)
    ax3.set_ylabel("frame length",fontsize=12)
    ax3.set_zlabel("average network join time",fontsize=12)   

    # 找到每个x值对应的z值最低的点的索引
    min_z_indices = []
    for xi in np.unique(x):
        mask = x == xi
        min_z_index = np.argmin(z[mask])
        min_z_indices.append(np.where(mask)[0][min_z_index])

    # 高亮每个x值对应的z值最低的点
    ax3.scatter(x[min_z_indices], y[min_z_indices], z[min_z_indices], c='r', marker='o',s=120, label='Min Z Points for each Agent Number')
    ax3.legend()
    ax3.view_init(elev=13, azim=-170)

    # 总路径最优度
    x = agent_total
    y = frame_length
    z = sum_actural_vs_optimal
    ax4 = fig.add_subplot(2, 2, 4, projection='3d')
    ax4.scatter(x, y, z, c=z, cmap='viridis', marker='o')
    ax4.plot_trisurf(x,y,z, cmap='viridis', alpha=0.5)
    ax4.set_title("total path efficiency ratio",y=0.92,fontsize=12)
    ax4.set_xlabel("agent number",fontsize=12)
    ax4.set_ylabel("frame length",fontsize=12)
    ax4.set_zlabel("total path efficiency ratio",fontsize=12)   

    ax4.set_zlim(1.0,2.0)

    # 找到每个x值对应的z值最低的点的索引
    min_z_indices = []
    for xi in np.unique(x):
        mask = x == xi
        min_z_index = np.argmin(z[mask])
        min_z_indices.append(np.where(mask)[0][min_z_index])

    # 高亮每个x值对应的z值最低的点
    # ax4.scatter(x[min_z_indices], y[min_z_indices], z[min_z_indices], c='r', marker='o',s=120, label='Min Z Points for each Agent Number')
    ax4.legend()
    ax4.view_init(elev=13, azim=-170)
    

    plt.tight_layout()
    plt.show()
    '''
    

    
    


if __name__ == "__main__":
    main()
