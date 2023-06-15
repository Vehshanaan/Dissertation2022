class plan():
    '''
    计划类。
    '''

    def __init__(self, frame_length) -> None:

        # 初始化帧长度
        self.frame_length_ = frame_length

        # 本节点的计划，其中成员为若干个坐标，越靠开头越是下一步该执行的
        self.my_plan_ = [None for _ in range(self.frame_length_)]

        # 接收到的计划保存数组：
        # - 外层组织： [时间片数目 = 帧长度]
        # - 内层组织： [本时间片中被占用的坐标]
        self.received_plan_ = [[] for _ in range(self.frame_length_)]、

        

    # 函数：输入[(坐标)], 返回适于发送的一维数组
    # 函数：输入接收到的一维数组，解码成[(坐标，counter)]
    # 函数：根据收到的[（坐标)，counter]记录其他节点的计划：每个时间片一个数组，数组中是此时间片中被占用的格子
    # 函数：输入时间片标号，返回[(此时间片中不可用的坐标)]
