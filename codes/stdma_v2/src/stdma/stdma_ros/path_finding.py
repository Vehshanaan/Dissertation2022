from heapq import heappop, heappush

def find_path(map, max_steps, start=(0,0), goal=(3,3)):

    start = tuple(start)
    goal = tuple(goal)

    # 使用优先级队列来保存待探索的节点，优先级由估计的路径长度决定
    queue = [(heuristic(start, goal), 0, start, [])]
    visited = set([start])

    while queue:
        _, cost, current, path = heappop(queue)

        if len(path) >= max_steps:
            continue

        if current == goal:
            return path + [current]

        neighbors = get_neighbors(current, map)
        for neighbor in neighbors:
            if neighbor not in visited:
                new_cost = cost + 1
                heappush(queue, (new_cost + heuristic(neighbor, goal), new_cost, neighbor, path + [neighbor]))
                visited.add(neighbor)

    # 终点被阻挡时，返回路径中距离终点最近的位置
    if path:
        return path

    return []

def get_neighbors(pos, map):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 上下左右四个方向
    neighbors = []

    for direction in directions:
        new_pos = (pos[0] + direction[0], pos[1] + direction[1])
        if is_valid(new_pos, map):
            neighbors.append(new_pos)

    return neighbors

def is_valid(pos, map):
    rows = len(map)
    cols = len(map[0])

    if 0 <= pos[0] < rows and 0 <= pos[1] < cols:
        if map[pos[0]][pos[1]]:
            return True

    return False

def heuristic(pos, goal):
    # 使用曼哈顿距离作为启发式估计
    return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])


def main():
    
    # 创建一个示例地图
    map = [
        [True, True, False, True],
        [True, True, True, True],
        [True, True, False, False],
        [True, True, False, True],
        [True, True, True, True],
    ]

    max_steps = 8  # 限制路径最大长度为5

    # 使用算法寻找路径
    path = find_path(map, max_steps)

    # 打印路径
    if path:
        print("路径：")
        for step in path:
            print(step)
    else:
        print("找不到路径。")
        
if __name__ == "__main__":
    main()