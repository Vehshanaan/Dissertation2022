import cv2

map_path = "/mnt/a/OneDrive/MScRobotics/Dissertation2022/codes/benchmarks/realworld_streets/street-png/Berlin_1_256.png"


def map_load(map_path):
    '''
    读取地图的函数

    Args:
        map_path (str): 地图文件的绝对路径

    Returns:
        map ([[T/F]]): 代表地图的二维列表，其中True代表可通过，False代表障碍物
    '''
    img = cv2.imread(map_path,0)
    _,img = cv2.threshold(img,0,255,cv2.THRESH_BINARY | cv2.THRESH_OTSU) # 大津法二值化 
    map = (img!=0).tolist()

    return map

def plan_compressor(node_id, plan2d) -> list:
    '''
    将[[x1,y1],[x2,y2],...]格式的二维数组压缩成一维的函数

    Args:
        node_id: 发送者编号
        plan (list[list]): [[x1,y1],[x2,y2],...]格式的二维数组

    Returns:
        result: 格式为[node_id,x1,y1,x2,y2,...]的一维数组
    '''
    if not plan2d:  # 如果输入为空列表
        return [node_id]  # 返回无计划的列表
    else:
        plan1d = [node_id]
        for _ in plan2d:
            plan1d.append(_[0])
            plan1d.append(_[1])


    return plan1d


def plan_decompressor(plan1d):
    '''
    将格式为[节点id, x1,y1,x2,y2...]格式的数组还原为 发送者id，[[x1,y1],[x2,y2],...] 的两个输出

    Args:
        plan1d (list): [节点id,x1,y1,x2,y2...]格式的一维数组

    Returns:
        node_id: 发送者id

        plan2d: [[x1,y1],[x2,y2],...]格式的二维数组
    '''
    if not plan1d:
        return -1, [[]]  # 如果输入为空，返回空, id写-1
    else:
        plan2d = []
        node_id = plan1d.pop(0)
        for i in range(0, len(plan1d), 2):
            plan2d.append((plan1d[i], plan1d[i+1]))
    return node_id, plan2d


if __name__ == "__main__":
    map_load(map_path)
