# 寻路类

from heapq import heappush, heappop
import time as t


class PathFinder():
    def __init__(self, map, num_slots, start, goal):
        self.map = map
        self.num_slots = num_slots
        self.start = start
        self.goal = goal
        self.others_plans = {}  # 别人的计划
        self.others_pos = {}  # 别人的位置
        self.current_pos = None  # 此时此刻自己的位置
        self.published_plan = []  # 已经投入运行的计划
        self.visited = []  # 已扩展过的点，是寻路算法的内存
        self.possibility = []  # 待扩展点，是寻路算法的内存
        self.current_time = 0  # 当前时间。内部时钟。用来给各种计划做时间索引，每槽过去就+1

    def reset(self):
        '''
        发生重大错误时的类重置，重置一切，除了绝对不会变的东西
        '''
        self.published_plan = []
        self.phantom_plan = []
        self.visited = []
        self.possibility = []

    def init(self):
        '''
        talker在end中，如果self==in 且刚刚结束的一帧属于自己且未入图时调用
        初始化自己的可能性
        '''

        # 计划的第一格时间
        start_time = self.current_time+self.num_slots+1  # 额外+1是因为发送计划的下一槽才动

        self.possibility = [(self.heuristic(self.start, self.goal),
                             start_time, (self.start[0], self.start[1], start_time), [(self.start[0], self.start[1], start_time)])]

        self.visited = []  # 连这个也顺手重置了吧

    def receive_plan(self, node_id, plan):
        plan_3d = []
        begin_time = self.current_time+self.num_slots+1  # 试出来就是这个，回头再想为什么吧
        for pos in plan:
            pos_3d = (pos[0], pos[1], begin_time)
            plan_3d.append(pos_3d)
            begin_time += 1
        if plan_3d:
            self.others_plans[node_id] = plan_3d  # 加到计划保存变量中

        # TODO: 用收到的计划来对已有的路径（可能性）进行切割
        self.react_to_plan(node_id, plan_3d)

    def react_to_plan(self, node_id, plan_3d):
        # 每次收到计划时对收到的计划作出反应，切除自己路径中所有冲突的部分
        avaliable_possibility = []
        for poss in self.possibility:
            my_plan = poss[3]  # 我的路径（3d）
            # 把计划剪成可用的计划
            avaliable_plan = self.trim_plan(my_plan, plan_3d)
            # heuristic(无冲突点，终点)， 无冲突点[-1], 无冲突点，[...，无冲突点]
            if avaliable_plan:
                avaliable_possibility.append((
                    self.heuristic(avaliable_plan[-1], self.goal),
                    avaliable_plan[-1][-1],
                    avaliable_plan[-1],
                    avaliable_plan
                ))
        self.possibility = avaliable_possibility

    def trim_plan(self, my_plan, other_plan):
        # 输入两计划，返回修剪后的我的计划
        my_dict = {t: (x, y) for x, y, t in my_plan}
        other_dict = {t: (x, y) for x, y, t in other_plan}
        for i, (x, y, t) in enumerate(my_plan):
            if t in other_dict and (x, y) == other_dict[t]:
                return my_plan[:i]
            if t+1 in other_dict and t+1 in my_dict and (x, y) == other_dict[t+1] and (my_dict[t+1][0], my_dict[t+1][1]) == (other_dict[t][0], other_dict[t][1]):
                return my_plan[:i]
        return my_plan

    def connive(self, time_limit):
        if not self.possibility:
            return  # 没有可能性的话：直接返回
        # TODO:什么情况会没有可能性呢？

        # 就是寻路算法中while的部分
        begin_time = t.time()  # 开始谋的时间
        while t.time() - begin_time < time_limit*0.5:
            if self.possibility:  # 如果自己的堆不空：
                _, time, current_pos, path = heappop(self.possibility)
                if (current_pos[0], current_pos[1]) == self.goal:  # 如果当前路径的尾部就是自己的终点：
                    # 把推出来的解还回去
                    heappush(self.possibility, (_, time, current_pos, path))
                    # 直接结束
                    return
                # 获得邻居点
                neighbors = self.get_neighbors(current_pos)
                # 对于所有的邻居：推入queue
                for neighbor in neighbors:
                    new_time = time+1
                    if neighbor not in self.visited:
                        heappush(self.possibility, (new_time+self.heuristic(neighbor,
                                 self.goal), new_time, neighbor, path+[neighbor]))
                        self.visited.append(neighbor)
            else:
                # 自己的可能性空了？什么情况下会空呢？
                return

    def cut_plan(self, required_length):
        # 从未来中选取头一位，截出计划，返回
        if not self.possibility:
            return None
        total_cost, time, last_pos, path = heappop(self.possibility)

        total_plan = self.published_plan+path
        # 将路径的前n个切下来
        plan = total_plan[:required_length]

        # 如果路径不够长，用路径最后一位补齐长度?

        # 将切完剩下的路径压入
        self.possibility = []
        self.visited = []
        heappush(self.possibility, (total_cost, time,
                 total_plan[-1], total_plan[required_length:]))
        # 保存切下的路径，为后续处理准备好
        self.published_plan = plan
        result = [(pos[0], pos[1]) for pos in plan]
        return result

    def slot_end(self):
        '''
        每次一个槽结束时调用,功能有：
         - 时间前进一位
         - 清理计划：自己的和别人的
         - 更新别人的位置记录
        '''
        # 时间前进一位
        self.current_time += 1

        # 更新自己的位置
        if self.published_plan:
            self.current_pos = self.published_plan.pop(0)

        # 更新别人的位置
        for node_id, plan in self.others_plans.items():
            # 符合此时刻的位置
            time_match = [pos for pos in plan if pos[-1]
                          == self.current_time]
            # 记录位置
            if time_match:
                self.others_pos[node_id] = time_match[0]

    def heuristic(self, pos1, pos2):
        return abs(pos1[0]-pos2[0])+abs(pos1[1]-pos2[1])

    def get_neighbors(self, pos):
        # 返回一个点可能的邻居点
        # 先生成所有可能点
        directions = [(1, 0), (-1, 0), (0, 0), (0, 1), (0, -1)]
        all_possible_neighbors = []
        for dir in directions:
            all_possible_neighbors.append(
                (
                    pos[0]+dir[0],  # 横向
                    pos[1]+dir[1],  # 纵向
                    pos[2]+1  # 时间

                )
            )

        # 去除墙里
        not_in_walls_neighbors = []
        for nei in all_possible_neighbors:
            x = nei[0]
            y = nei[1]
            if x < len(self.map[0]) and y < len(self.map) and x > -1 and y > -1:
                if self.map[y][x]:
                    not_in_walls_neighbors.append(nei)
        # 去除碰撞
        no_collision_neighbors = []

        for nei in not_in_walls_neighbors:  # 对于上一步生成的所有相邻点
            # 在自己收到的所有计划中寻找此点是否位于计划中
            if any(nei in plan for plan in list(self.others_plans.values())):
                pass
            else:
                no_collision_neighbors.append(nei)

        # 去除swap
        no_swap_neighbors = []

        for nei in no_collision_neighbors:
            append = True
            # 如果有谁的下一步在二维空间上==pos,且其当前位置为nei(二维意味):swap发生了。
            for plan in list(self.others_plans.values()):
                # 如果谁的下一步==pos,即pos[2]+1在计划中：
                if (pos[0], pos[1], pos[2]+1) in plan:
                    # 如果nei[2]-1也在计划中：
                    if (nei[0], nei[1], nei[2]-1) in plan:
                        # swap发生了
                        append = False
            if append:
                no_swap_neighbors.append(nei)

        return no_swap_neighbors
