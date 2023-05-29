# 在此文件中可以用井号插入注释

# 加入一个标准消息接口std_mags 下的string

std_msgs/String content

# 加入一个Image类型

sensor_msgs/Image image


# 所有消息类型都是由原始数据类型构成。包括上述调用的两个类型也是。
# String是int32和string构成，image是string，uint8，uint32构成

# 原始数据类型：
# bool,byte,char,float32,float64,int8,uint8,int16,uint16,32,64,string

# 数据类型的用法就像程序里的变量类型，后面加中括号就可以直接变成数组，而且非原始的数据类型也可以这么用

# 所以其实还有一种写法，就是自己用最原始的原始数据类型来搭建：

# string content
# sensor_msgs/Image image

# 写完这个后面记得下一步就是改CmakeLists.txt