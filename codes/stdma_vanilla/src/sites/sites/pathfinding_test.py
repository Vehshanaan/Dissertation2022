import heapq

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.g = 0  # 实际代价
        self.h = 0  # 启发函数估计值
        self.f = 0  # 总代价
        self.parent = None

    def __lt__(self, other):
        return self.f < other.f

def calculate_distance(node, target):
    return abs(node.x - target.x) + abs(node.y - target.y)

def find_path(grid, start, target):
    rows = len(grid)
    cols = len(grid[0])

    # 定义四个方向的移动
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    open_set = []
    closed_set = set()

    start_node = Node(start[0], start[1])
    target_node = Node(target[0], target[1])

    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)
        closed_set.add((current_node.x, current_node.y))

        # 到达目标节点，重构路径并返回
        if current_node.x == target_node.x and current_node.y == target_node.y:
            path = []
            while current_node:
                path.append((current_node.x, current_node.y))
                current_node = current_node.parent
            return path[::-1]

        for direction in directions:
            next_x = current_node.x + direction[0]
            next_y = current_node.y + direction[1]

            # 忽略越界和障碍物
            if next_x < 0 or next_x >= rows or next_y < 0 or next_y >= cols or grid[next_x][next_y] == 0:
                continue

            neighbor = Node(next_x, next_y)
            neighbor.g = current_node.g + 1
            neighbor.h = calculate_distance(neighbor, target_node)
            neighbor.f = neighbor.g + neighbor.h
            neighbor.parent = current_node

            # 如果邻居节点已经在关闭集合中，跳过
            if (neighbor.x, neighbor.y) in closed_set:
                continue

            # 如果邻居节点已经在开放集合中，更新其代价
            for open_node in open_set:
                if neighbor.x == open_node.x and neighbor.y == open_node.y:
                    if neighbor.g < open_node.g:
                        open_node.g = neighbor.g
                        open_node.f = neighbor.f
                        open_node.parent = neighbor
                    break
            else:
                heapq.heappush(open_set, neighbor)

    # 无法找到路径
    return []

# 示例用法
grid = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0]
]
start_pos = (0, 5)
target_pos = (0, 0)

path = find_path(grid, start_pos, target_pos)
if path:
    print("最优路径：", path)



else:
    print("无法找到路径")
