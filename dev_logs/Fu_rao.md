# 7.14

- 和指导老师进行模拟答辩，对工作已进行改进

- 调整项目样式，最终效果如图

  ![image-20220714151615038](https://raw.githubusercontent.com/FRYBCDL/test1/master/test1/image-20220714151615038.png)

  ![image-20220714151722658](https://raw.githubusercontent.com/FRYBCDL/test1/master/test1/image-20220714151722658.png)

  ![image-20220714151741281](https://raw.githubusercontent.com/FRYBCDL/test1/master/test1/image-20220714151741281.png)

  ![image-20220714151834146](https://raw.githubusercontent.com/FRYBCDL/test1/master/test1/image-20220714151834146.png)

  ![image-20220714151859974](https://raw.githubusercontent.com/FRYBCDL/test1/master/test1/image-20220714151859974.png)



# 7.13

对项目实训工作进行收尾、总结

# 7.12

- 尝试比较迁移学习和自己编写的resnet18准确率，结果如下

  迁移学习：

  ![image-20220713205103216](https://raw.githubusercontent.com/FRYBCDL/test1/master/test1/image-20220713205103216.png)

![image-20220713205214166](https://raw.githubusercontent.com/FRYBCDL/test1/master/test1/image-20220713205214166.png)

不使用迁移学习：

![image-20220713205609942](https://raw.githubusercontent.com/FRYBCDL/test1/master/test1/image-20220713205609942.png)

![image-20220713205629802](https://raw.githubusercontent.com/FRYBCDL/test1/master/test1/image-20220713205629802.png)

可以看出，不使用迁移学习一开始loss比迁移学习方法的loss大很多，最终的准确率效果也不如迁移学习。

# 7.11

- 调参
- 对输入的图像进行小角度随机旋转、resize、裁剪等处理
- 阅读resnet18有关资料，编写resnet18网络代码

# 7.10

- 编写实验代码，修改bug
- 进行迁移学习，尝试使用resnet18进行多分类，验证集测试结果如下：

第一次:![image-20220704161739485](https://raw.githubusercontent.com/FRYBCDL/test1/master/test1/image-20220704161739485.png)

第二次：![image-20220705000003245](https://raw.githubusercontent.com/FRYBCDL/test1/master/test1/image-20220705000003245.png)

准确率大概在0.9左右

# 7.9

- 成功生成csv文件，方便后续处理

  ![image-20220713174514331](https://raw.githubusercontent.com/FRYBCDL/test1/master/test1/image-20220713174514331.png)

- 编写实验代码



# 7.8

- 继续编写读取数据部分的代码，并修改bug

- 对数据集进行7个类别的划分

  ![image-20220713172846498](https://raw.githubusercontent.com/FRYBCDL/test1/master/test1/image-20220713172846498.png)

  

# 7.7

- 开始尝试多分类模型，拟定使用resnet18，并且尝试比较迁移学习和自己编写的resnet18准确率
- 进行读取数据部分的代码编写

# 7.6

- 修改代码bug，对于老师昨天提出的问题进行了实验验证。
- 获得实验结果：用开闭操作判断图像是否完整的准确率为0.9700854700854701；处理一张图片的用时为0.031238794326782227s

但是由于图像处理只能针对本次问题，如果处理新问题时，图像处理需要重新编写代码，没有网络模型的普适性，由此我们权衡考虑打算直接使用神经网络进行分类

# 7.5

- 今日开会，老师对于我们之前用图像处理识别不完整图像的工作提出了建议：我们想当然的觉得用传统图像处理的方式一定会比机器学习更快速而且可以一定程度上精简数据，提高模型准去率，但是缺少了实验验证的环节（没有进行时间比对）并且没考虑准确率损失问题。
- 针对老师提出的问题编写代码，进行实验验证。

# 7.4

- 模拟实际生产中，相机会出现的问题：(i)颜色不正；(ii)噪点多；(iii)图像过暗；(iv)图像过曝；(v)镜头畸变

- 颜色不正：这个问题对于我们的项目来说并不重要，因为最终都会转为二值图

  噪点过多：我们考虑在数据集中加入高斯噪声来模拟，并在数据输入时增加去噪操作（均值滤波、高斯滤波、中值滤波）

  ![image-20220714005823449](https://raw.githubusercontent.com/FRYBCDL/test1/master/test1/image-20220714005823449.png)
  
  ![image-20220714005704742](https://raw.githubusercontent.com/FRYBCDL/test1/master/test1/image-20220714005704742.png)
  
  图像过暗、过曝：我们会将RGB通道转为HSV（色调H，饱和度S，明度V），调节V的值使图像有过度曝光的效果，将这些数据加入数据集；并在数据处理时增加直方图处理的操作

<img src="https://raw.githubusercontent.com/FRYBCDL/test1/master/test1/image-20220714003910624.png" alt="image-20220714003910624" style="zoom:67%;" /><img src="https://raw.githubusercontent.com/FRYBCDL/test1/master/test1/image-20220714003947490.png" alt="image-20220714003947490" style="zoom:67%;" />

​      镜头畸变：鱼眼镜头及鱼眼矫正，不过效果不太好

![image-20220714004053128](https://raw.githubusercontent.com/FRYBCDL/test1/master/test1/image-20220714004053128.png)

# 7.2

- 由于缺陷检测只需要关注螺丝的部分，因此尝试闭操作后加上一步开操作，然后统计符合面积范围的点的个数，由此判断是否不完整，效果比前几种方法好很多，该功能基本实现：

  <img src="https://raw.githubusercontent.com/FRYBCDL/test1/master/test1/image-20220714003039015.png" alt="image-20220714003039015" style="zoom: 67%;" /><img src="https://raw.githubusercontent.com/FRYBCDL/test1/master/test1/image-20220714004235755.png" alt="image-20220714004235755" style="zoom: 67%;" />

# 7.1

- 根据前两种方法的尝试，认为问题出现在检测到的边缘不够连续，造成很多微小的连通域影响判断，因此在选择矩形前增加了对图像的闭操作，获得了比之前更好的效果。

- ![image-20220714004423560](https://raw.githubusercontent.com/FRYBCDL/test1/master/test1/image-20220714004423560.png)![image-20220714004342391](https://raw.githubusercontent.com/FRYBCDL/test1/master/test1/image-20220714004342391.png)

- 但是存在问题：对于不完整但不影响整体判断的图像识别有误

  ![image-20220714004357292](https://raw.githubusercontent.com/FRYBCDL/test1/master/test1/image-20220714004357292.png)

  

# 6.30

- 对图像进行二值化->提取图像中的直线->判断两直线夹角余弦，但是同样提取的直线是断断续续的，效果也不好。由于图片画质因素，很多看似是直线的也未检测出是直线，还有许多散碎的直线并没有连接成长线，此外还有很多噪声直线。

<img src="https://raw.githubusercontent.com/FRYBCDL/test1/master/test1/image-20220714004438290.png" alt="image-20220714004438290" style="zoom:50%;" /><img src="https://raw.githubusercontent.com/FRYBCDL/test1/master/test1/image-20220714004447273.png" alt="image-20220714004447273" style="zoom:50%;" /><img src="https://raw.githubusercontent.com/FRYBCDL/test1/master/test1/image-20220714004506601.png" alt="image-20220714004506601" style="zoom:50%;" />



# 6.29

- 识别不完整图像：对图像进行二值化->提取图像边缘->定位四边形->判断两两相邻直线夹角余弦是否在90°左右。但是效果不好，并没有识别出整体的工件边缘。

  ![image-20220702091723770](https://raw.githubusercontent.com/FRYBCDL/test1/master/test1/image-20220702091723770.png)



# 6.28

- 开组会，明确下一步工作方向：对图像添加噪声。由于我们现在的图像都是质量很好的图像，所以尽管当前的训练很好，但是模型的鲁棒性可能不高。
- 考虑给图像过曝、过暗、添加噪声（高斯、椒盐等）
- 开会时老师也建议我们对于缺角的图像识别后可以给用户一个反馈，考虑可以使用图像处理的方式。



# 6.27

- 学习tensorflow

  

# 6.26

- 考虑到老师开会时所说可以记录不同缺陷类型的组件数量，以便更加直观的反馈。由此除了基本版本外，还设计了可视化的界面，后续时间充裕的话尝试实现。（图中数据非实际开发中的数据，仅供展示使用）

![image-20220702090157083](https://raw.githubusercontent.com/FRYBCDL/test1/master/test1/image-20220702090157083.png)



# 6.25

- 实现web前端css代码编写

![image-20220702090147563](https://raw.githubusercontent.com/FRYBCDL/test1/master/test1/image-20220702090147563.png)

![image-20220702090210870](https://raw.githubusercontent.com/FRYBCDL/test1/master/test1/image-20220702090210870.png)

# 6.24

- 设计web前端CSS原型

# 6.23

- 和小组同学沟通后，决定使用旋转、反转的方式进行数据增强，将数据增加至原来的6倍
- 由于训练网络的同学反馈当前数据训练效果很好，因此暂不考虑小样本训练和GAN生成图像



# 6.22

- 统计图像类别：class：one 1（13个）；neighbor_two 2（18个）；diagonal_two 3（20个）；three 4（22个）；four 5（14个）；good 6（17个）；imperfect 7（13个）

- 完成初步数据分类、旋转和格式转换等操作

- 和负责搭建网络的同学进行沟通明确具体处理数据的方向

- 针对样本过少的问题提出三种解决思路：通过神经网络进行图像生成、转化为小样本问题、通过图像处理技术生成图片。

- 阅读有关小样本方面的论文以及源码，Jake Snell, Kevin Swersky, and Richard Zemel. Prototypical networks for few-shot learning. In NeurIPS, pages 4077–4087, 2017.了解了小样本流程，发现处理方法有可取之处但也有不匹配我们问题的地方。

- 原型网路：

  代码地址：https://github.com/yinboc/prototypical-network-pytorch

  论文原文：https://arxiv.org/abs/1703.05175#:~:text=Prototypical networks learn a metric space in which,in this limited-data regime%2C and achieve excellent results.

# 6.21

- 开会中明确了项目目标、角色和项目技术点
- 小组讨论时确定我在算法组，主要负责数据处理相关工作。

