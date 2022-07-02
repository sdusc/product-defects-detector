# 旋转图像名称写入文件，方便处理
import pandas as pd
import os

path = r'C:\Users\FR\PycharmProjects\pythonProject\summerProject\data\DPdata.csv'
# 使用pandas读入
data = pd.read_csv(path)  # 读取文件中所有数据
# 读取某一列
y = data[['name']]
print(y)
rots = ['rot000', 'rot090', 'rot180', 'rot270']
file = open(r'C:\Users\FR\PycharmProjects\pythonProject\summerProject\data\data_rot.txt', 'a')
for i in y.values:
    i = str(i)
    for j in rots:
        print(str(i[2:5]) + os.sep + str(j))
        file.write(i[2:5]+os.sep+str(j)+'\n')
