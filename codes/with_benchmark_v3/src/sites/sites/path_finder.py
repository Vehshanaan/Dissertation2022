from heapq import heappop, heappush
import time

from codes.benchmarks.scene_generator import heuristic

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

class PathFinder():
    def __init__(self, map, num_slot, start, goal):
        self.map = map # 代表地图的二维数组
        self.num_slot = num_slot # 帧长度
        self.start = start # 每次寻路时的起点
        self.goal = goal # 终点
        self.queue = None # 寻路所使用的堆
        self.path = [] # 生成的路径 在幻想中走过的路

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

    def path_find(self, time_limit, plan):

        start_time = time.time() # 开始筹谋的时刻

        # 先检查计划和已生成的路径之间有没有冲突，若有冲突，剪掉已生成的路径的后面
        if self.path: # 如果自己的路径不为空
            for plan in plan.values(): # 对于每个计划：
                self.path = cut_path(self.path,plan) # 将有重复的部分全部剪掉
                # 清除该清除的部分，重新开始
        
        # 读取上次的工作, 继续
        
        
        
        


        # 用自己的起点和收到的计划计算一个路径
        # 生成的路径的终点保存为起点
        # 生成的路径记得保存
    def path_return(self):
        # 根据要求，从已生成之计划中截取开头的若干位，作为返回量
        # 若计划长度不达标，则将尾部用最后一位补足
        # 更新自身状态？ 
