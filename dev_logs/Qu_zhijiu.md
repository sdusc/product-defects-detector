# 开发日志
## 2022-7-15：
+ 准备答辩稿，同时将模型交给后端同学部署
+ 将模型的对比数据进行了总结
+ 成功答辩，解题！
## 2022-7-14：
+ 在不断的调试与优化过程中完成了对我们任务的优化
+ 上午进行了答辩预演
+ 写好了使用pb文件进行推理的代码
+ 解决了duration以秒为单位的问题
+ 成功从300ms降到了5ms左右，优化了60倍，大功告成
## 2022-7-13：
+ 完成对tensorflow的框架转换
+ 我与模型组同学对接
+ 最终确定以在其电脑上训练保存h5文件，然后我读入h5模型并保存pb进而开始优化
## 2022-7-12：
+ 继续研读文档
+ 下午开答疑会汇报本周工作
## 2022-7-11：
+ 继续阅读代码
+ 同时等待模型组同学训练好tensorflow的模型
## 2022-7-9：
+ 整理了搞好的部分的全部代码
+ 与队友进行交流讨论之前完成的工作和后续要完善的工作
## 2022-7-8：
+ 搭建了vgg16的预训练模型
+ 将处理好后的工业品图片数据集输入到模型训练并保存好pb文件
+ 将fp32的模型文件进行量化报错
+ 将输入tensor的shape调整后重新量化成功
## 2022-7-7：
+ 进行了debug，首先确定转换后的onnx模型是没有问题的
+ 而在读入pb文件时，确认正确的pb文件可以正常读入而转换后的pb文件无法正常读入
+ 在研究了报错之后大概明白问题出在onnx-tf的过程中，可能对某些特殊模型无法这样转换
## 2022-7-6：
+ pytorch-onnx是有官方文档的，对照着进行尝试主要把input_size=(224,224,3)搞好就没有问题
+ 导出的onnx再使用onnx-tf向pb模型转
+ 但转换完成后pb模型无法像其他模型一样被读入
## 2022-7-5：
+ 先学习了算法组给出的模型参数以及对模型数据的处理，然后使用pth模型进行了预测
+ 由于暂时还没有tensorflow版本的模型，所以打算首先尝试将pth模型转成pb
+ 使用方法是pytorch-onnx-tensorflow
+ 开始转换
## 2022-7-4：
+ 租用了新的intel xeon至强芯片，以及更新了neural-compressor要求的新版本环境（ubantu，tensorflow，opencv等）
+ 成功使用之前训练好的fp32模型进行量化
+ 将量化好的int8模型文件保存好，后面打算先与之前的fp32模型进行性能比对
## 2022-7-2：
+ 使用minist_dataset的现成数据集
+ 在极链上租用了2080服务器训练
+ 将训练好的fp32模型保存好
+ 在量化的过程中出现了环境问题，解决ing
## 2022-7-1：
+ 尝试在本地从搭建网络开始实现
+ 搭建了vgg16的网络，找了数据集，调整了参数
+ 阿里云的服务器内存不够用，无法训练，失败
+ 后面直接使用alexnet的网络结构
## 2022-6-30：
+ 备考期末考试
## 2022-6-29：
+ 边看文档边看实例
+ 跟随着实例一步一步学习
## 2022-6-28：
+ 上午把曾经做的demo转移到自己的阿里云服务器
+ 配好环境之后一次运行成功
+ 继续在看文档中理解整个pipeline的细节
+ 开始关注到模型保存pb格式文件的问题
+ 下午开会在和老师交流的过程中了解了例子中的优化过程的数据集的功能
## 2022-6-27：
+ 分门别类的阅读文档
+ 在初步的对整个工作的pipeline有一个比之前深刻的认识
+ 主要尝试研究yaml文件
## 2022-6-25：
+ 今天image-net.org网站修复了，然后继续使用那个example来试，发现需要下载500G的数据，所以这个example的尝试允许就暂罢。
+ 碰壁这么多次之后回去细看了文档
+ 与队友重新讨论后，拨乱反正之后进行了重新分工以继续进行后续的工作，是一个阶段性开始
+ 晚上与队友进行了阶段性会议进行了总结
## 2022-6-24：
+ 在本地ssh连接了devcloud继续进行demo的运行
+ 在做例子中的demo时卡在了image-net.org网站崩掉了
+ 换到不需要下载image-net数据集的例子来搞，然后环境问题导致无法运行，后续环境搞好之后变成网络无法使用，devcloud还是有些不稳定
## 2022-6-23：
+ 创建了intel平台的账号
+ 在给的服务器上下载了所需代码
+ 尝试运行了给出的demo
## 2022-6-22：
+ 研究了ppt和任务pdf，对我的任务部分--优化，有了大概的了解
+ 搞清楚了任务的本质是对模型建立好之后的训练的速度的优化
+ 根据优化方法细化了分工明确了小目标
+ 实验并确定了开发测试平台就是intel的devcloud
+ 准备好了模型以及文档为后续的开发作准备
## 2022-6-21：
+ 总结了自己的问题并于队友进行了交流
+ 参与了项目工程师的开题讲解和答疑
+ 晚上小组开会确定了任务分工
## 2022-6-20：
+ 参加了开题会议，试打卡
+ 下午就研读了任务pdf
+ 参加了intel工程师举行的宣讲会

