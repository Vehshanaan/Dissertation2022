# slot数据的格式，采用topic进行此类数据的传输

int16 slot_no # 当前slot的编号，从1开始

int16 slot_total # 一帧有多少个slot

int16 sender_no # 当前发送者编号（“node几的那个几”）

bool occupied # 此slot是否有主