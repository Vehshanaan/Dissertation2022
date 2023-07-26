from heapq import heappop, heappush
import time


def cut_path(path,plan):
    '''
    根据传入的计划中的最新的碰撞点切割已有的自己计划

    Args:
        path (list): 自己的计划
        plan (list): 别人的计划

    Returns:
        path_modified: 处理后的计划
    '''
    min_length = min(len(path),len(plan))
    indices = [i for i in range(min_length) if path[i]==plan[i]]
    if indices:
        path = path[:indices[0]]
    return path

class MyPathFinder():
    def __init__(self, map, num_slot, start, goal):
        self.map = map # 代表地图的二维数组
        self.num_slot = num_slot # 帧长度
        self.start = start # 节点起点
        self.goal = goal # 终点
        self.path = [] # 生成的路径 在幻想中走过的路
        self.joined = False # 是否已加入网络

    def update(self):
        '''
        每次移动后调用，作用是弹掉路径的第一位，如果有路径的话
        '''
        if self.path: self.path.pop(0)
        # 这样路径的开头和其他计划的开头就对齐了
    
    def reset(self):
        '''
        抹去寻路算法的存档，从头开始
        '''
        self.queue = None

    def heuristic(self,pos, goal):
        # 使用曼哈顿距离作为启发式估计
        return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])
        
    
    def transpose_list(input_list):
        '''
        将输入的二维列表中的成员列表的每个相同位置的元素放进一个列表最后打包成一个新二维列表的函数
        '''
        if not input_list:
            return None
        num_rows = len(input_list)
        num_cols = max(len(row) for row in input_list)

        transposed_list = [[] for _ in range(num_cols)]
        for row in input_list:
            for col_index, element in enumerate(row):
                transposed_list[col_index].append(element)

        return transposed_list
    
    def is_valid(self, pos, map):  

        x = pos[0]
        y = pos[1]

        col_max = len(map)
        row_max = len(map[0])

        if 0 <= x < row_max and 0 <= y < col_max:
            if map[y][x]:
                return True

        return False
    
    def get_neighbors(self, pos, map, current_plan=[]):
        '''
        获得一个点周围可用的点

        Args:
            pos (tuple): 当前位置
            map (list[list]): 地图
            plan (list[tuple]): 下一步的计划，是主函数根据时间点从计划总保存变量中切割出来的一片。

        Returns:
            _type_: _description_
        '''
        directions = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]  # 上下左右四个方向和原地。
        neighbors = []

        for direction in directions:
            new_pos = (pos[0] + direction[0], pos[1] + direction[1])

            if self.is_valid(new_pos, map) and new_pos not in current_plan:  # 如果不在地图障碍物且不在别人的下一步计划中：
                neighbors.append(new_pos)

        return neighbors

    def remove_swap_collision_positions_first(self, current, neighbors_with_swaps, cost, plan_dict, others_positions):
        neighbors = []
        next_steps = {}
        if plan_dict:
            for node_id, plan in plan_dict.items():
                if cost < len(plan):
                    pos = plan[cost]
                    next_steps[node_id] = pos
        for neighbor in neighbors_with_swaps:
            add = True
            if next_steps:
                for node_id, pos in next_steps.items():
                    if pos == current:
                        if others_positions:
                            if others_positions[node_id] == neighbor:
                                add = False
            if add:
                neighbors.append(neighbor)
        return neighbors

    
    def remove_swap_collision_postions(self, current, neighbors_with_swaps, cost, plan_dict):
        neighbors = []
        # 先生成当前计划和上一步计划
        # 当前步计划
        next_steps = {}
        # 所有节点当前的位置（其实就是上一步计划）
        current_positions = {}
        if plan_dict:
            for node_id, plan in plan_dict.items():
                # 先提取当前步计划
                if cost < len(plan):  # 如果计划有那么长：
                    pos = plan[cost]
                    next_steps[node_id] = pos #tuple(pos)
                # 再提取之前步计划
                if cost-1 >= 0 and cost-1 < len(plan):
                    pos = plan[cost-1]
                    current_positions[node_id] = pos #tuple(pos)

        for neighbor in neighbors_with_swaps:
            add = True
            if next_steps:
                for node_id, pos in next_steps.items():
                    if pos == current:  # 如果有人的下一步是到我现在的位置
                        if current_positions:
                            # 如果此人的当前位置等于我下一步想去的位置
                            if current_positions[node_id] == neighbor:
                                add = False  # 这就是swap了，不行
            if add:
                neighbors.append(neighbor)

        return neighbors

    def path_find(self, time_limit, plan, others_positions, first_ever):

        self.joined = first_ever # 更新是否加入的状态

        start_time = time.time() # 开始筹谋的时刻

        # 先检查计划和已生成的路径之间有没有冲突，若有冲突，剪掉已生成的路径的后面
        if self.path: # 如果自己的路径不为空
            for plan in plan.values(): # 对于每个计划：
                self.path = cut_path(self.path,plan) # 将有重复的部分全部剪掉
                # 清除该清除的部分，重新开始
        
        # 读取起点
        if self.path:
            start = self.path[-1]
            start_time = len(self.path)
        else: 
            start = self.start
            start_time = 0

            # 处理一下输入的计划，变成以时间步划分的计划
        plan_no_id = list(plan.values())
        plan_no_id = self.transpose_list(plan_no_id)  # 转换完成

        queue = [(self.heuristic(start,self.goal),start_time,start,[])]
        visited = set([])


        time_left = time_limit - time.time()-start_time
        
        planning_start_time = time.time()

        while time.time()-planning_start_time<time_left*0.7: # queue里有东西且时间没用完：
            heuristic_cost, cost,current,path = heappop(queue)

            if current == self.goal:
                self.path+=path # 如果到达终点：直接保存生成的路径
                return # 直接结束
            
            current_others_plan = [] # 获取当前步的其他人计划
            if plan_no_id and cost<len(plan_no_id):
                current_others_plan = plan_no_id[cost]
            
            # 获得不上墙也不和别人碰的邻居点
            neighbors = self.get_neighbors(current, map, current_others_plan)

            # 如果是初次入网，起始点必须是起点
            if first_ever and cost==0:
                neighbors = [start]
            
            # 去除swap碰撞类型
            if cost!=0: # 对于非第一步的swap去除
                neighbors = self.remove_swap_collision_positions_first(current, neighbors, cost,plan, others_positions)
            else: # 对于非第一步的swap去除
                neighbors = self.remove_swap_collision_postions(current, neighbors, cost, plan)
            
            for neighbor in neighbors:
                new_cost = cost+1
                if tuple(list(neighbor)+[new_cost]) not in visited:
                    heappush(queue, (new_cost+heuristic(neighbor,self.goal),new_cost,neighbor,path+[neighbor]))
                    visited.add(tuple(list(neighbor)+[new_cost]))
        
        if queue: # 如果超时且queue不为空
            _,_,_,new_path = heappop(queue)
            self.path+=path # 将生成的路径加到已有路径后面




                         
    def path_return(self):
        # 根据要求，从已生成之计划中截取开头的若干位，作为返回量

        # 没有考虑self.path=None的情况！

        # 若计划长度不达标，则将尾部用最后一位补足
        if len(self.path)<self.num_slot:
            if not self.joined: return None # 如果没加入且没找到足够长的路径：return
            # 补长计划
            self.path = self.path+[self.path[-1]]*(len(self.path)-self.num_slot)
            path = self.path.copy()
            self.path = [path[-1]]  # 为了后续寻路有start可用
            return path
        else:
            path = self.path.copy()

            path = self.path[:self.num_slot] # 获取要发出去的计划

            self.path = self.path[self.num_slot:] # 切掉发出去的计划

            return path



        # 更新自身状态？ 
