# 开发日志-董书玮

## 2022.6.21

  参加暑期实训开题会议

- 下午13：30，参加由队长主持的队内的第一次全体线上会议，主要明确项目的内容、要点、技术、人员、分工等问题；
- 下午15：00，参加由英特尔的指导老师主持的答疑会，主要介绍了项目的专业内容、难点以及对我们的期望，并对我们的疑问做了悉心的回答。
- 晚上19：30，参加组内第一次线下全体会议，主要确定分工问题，并明确了项目的第一个里程碑。

## 2022.6.22
- 阅读论文：《工业品缺陷检测方法——综述》，阅读进度为50%。该论文主要对工业品缺陷检测的相关方法进行了概要性的阐述，比如传统的基于特征的机器视觉算法（基于纹理特征、基于颜色特征、基于形状特征）、基于深度学习的检测方法（监督方法、无监督方法、弱监督方法）以及缺陷检测可能遇到的关键问题（实时问题、小样本问题、小目标问题、数据不均衡问题）。论文链接https://www.mdpi.com/2076-3417/11/16/7657
- 通过阅读该论文，结合查询资料，使我对工业品缺陷检测以及相关的深度学习的方法有了基础的了解，相当于让本不熟悉深度学习的我入了门。
- 晚上19：30，参加线上组会，主要内容为汇报第一天的工作进度，判断分工是否合理，以及能否在里程碑前完成各自的任务。

## 2022.6.23

- 将论文《工业品缺陷检测方法——综述》阅读完，并对深度学习和目标检测算法有了初步的了解。
- 因队内未来考虑使用yolo进行目标检测，以提高检测精度，所以我在知网上找到一篇名为《智能装配中基于YOLO v3的工业零件识别算法研究》的论文，并通过阅读论文，试图发现一些yolo的优化方法，为之后yolo的使用和优化奠定基础，提供参考的优化方法。论文链接为https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CJFD&dbname=CJFDLAST2020&filename=GDZJ202010008&uniplatform=NZKPT&v=8PhFCQeAVyTWony9qymh2xyXKaUZFS2BpcRIiVbibehPK7wkPpin_hoVHs5aw8Tz

## 2022.6.24
- 将论文《智能装配中基于YOLO v3的工业零件识别算法研究》阅读完，了解了YOLO v3改进的方法：使用k-means算法重新聚类预选框的参数,残差网络来减少网络的参数,结合多尺度方法、采用Mish激活函数提高精确度,使其更适合工业零件的小目标分类检测。最终的实验结果表明与原有的YOLO v3算法对比,使用改进后的网络模型具有良好的鲁棒性,准确率提高了1.52%,时间提高了7.25 ms,实现精确实时地检测出智能装配系统中的零件种类。


## 2022.6.25

- 结合论文所介绍，主要学习了激活函数的相关知识，包括激活函数的定义、作用、常用的激活函数（Sigmoid、Tanh、Relu、Mish）、激活函数的公式以及图像，重点学习了Mish激活函数，阅读了创造Mish函数的原论文。了解到YOLO v3采用的是改进的Relu激活函数，而改为使用Mish可以提高准确性，缩短识别时间。Mish原论文的链接地址：https://arxiv.org/vc/arxiv/papers/1908/1908.08681v1.pdf
- 尝试使用Mish函数对YOLO v3进行优化
- 晚上19：30，参加组会，会议内容主要是各小组汇报各自一周的工作。我制作了PPT，详细介绍了YOLO v3的优化方法，以及Mish函数的相关内容。

## 2022.6.27

- 我们小组在开发过程中需要进行流程图、示意图、原型图等图像的绘制，因此我针对这些图像的画法进行了针对的学习。今天首先学习了原型图的绘制的基本知识，通过在网上找教程自学，使用原型图绘制软件Axure，掌握了原型图绘制的基本要求和基本画法。有了一个原型图绘制的基础入门。

## 2022.6.28

- 今天我的工作主要是在昨天原型图基础知识的基础上，尝试自己绘制一款软件的原型图。因为自己一直以来都想自己开发一款演唱会购票APP，所以本人就尝试使用新学习的原型图绘制的技能，绘制出来我对这款APP的初步构想。共计划绘制11个页面、11张原型图，今天实际绘制了七张，都是首页的相关内容：首页、动态内容页、他人主页、他人曾看的演出页、他人关注的人页、关注他的人页面以及私信页面，剩下的4张明天完成。
- 下午15：00，参加由英特尔的指导老师主持的第二次答疑会议，仔细聆听了老师对于我们目前进度的建议，以及对我们小组的一些困惑的点拨和解答。

## 2022.6.29

- 今天将剩下的4张原型图绘制完毕，至此关于自己设想的APP的11张原型图已经绘制完毕，对于原型图的绘制也有了一个比较熟练的掌握。
- 接下来在今天我又学习了结构图和流程图的画法，还是在网上寻找教程学习，结构图使用的是Xmind进行绘制，流程图的话使用的是web端的ProcessOn。

## 2022.6.30

- 今天我在昨天学习流程图和结构图绘制的基础上，自己尝试绘制了一些软件的系统流程图和功能结构图，掌握了流程图和结构图的绘制方法。
- 学习特征工程的相关知识，为我们项目对数据集进行特征提取和特征选择，了解了一些颜色提取的方法，包括颜色直方图，颜色相关图等。

## 2022.7.1

- 阅读论文《基于扇区邻域特征工程的玻璃封装绝缘端子缺陷检测》，了解到了缺陷检测的特征工程的方法。阅读进度百分之五十。
- 论文链接：https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CJFD&dbname=CJFDAUTO&filename=DZYX202205005&uniplatform=NZKPT&v=OBbwn4s_s_BoZd5GgmYNeM0Zhj1Dc2wht2bnqNSn8MCanMDHEE-3L8H2R_JAucWT

## 2022.7.2

- 准备中期答辩：制作中期答辩ppt，准备中期答辩材料，提供中期答辩的个人工作总结。

## 2022.7.4

- 上午9：30，参加中期答辩腾讯会议，以小组为单位汇报组内工作的情况，并认真聆听了算法组和组长关于项目核心算法和核心功能的讲解，对于项目的架构和技术栈有了更进一步的了解。

## 2022.7.5

- 下午15：00，参加由英特尔指导老师主持的第三次答疑会。
- 阅读论文《基于扇区邻域特征工程的玻璃封装绝缘端子缺陷检测》，深度了解了深度学习方法处理工业缺陷品的常用方法，包括预处理、粗分类、计算灰度变化率、计算反光特征、方向统计特征等等。
- 论文链接：https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CJFD&dbname=CJFDAUTO&filename=DZYX202205005&uniplatform=NZKPT&v=OBbwn4s_s_BoZd5GgmYNeM0Zhj1Dc2wht2bnqNSn8MCanMDHEE-3L8H2R_JAucWT

## 2022.7.6

- 小组长分配下来任务，需要我去画整个项目的功能结构图，并且画出来的结果需要展示在github的项目首页当中，因此我开始着手准备结构图的相关工作。
- 复习了几天前学习的使用Xmind绘制结构图的相关知识和技巧，并重点在网上学习了：怎么划分项目结构，怎么细分项目功能、又如何将细分后得到的细碎的小功能点进行整合。

## 2022.7.7

- 与小组长沟通结构图的需求、结构图的构想等需求问题。
- 向小组长询问项目的大体框架、具体结构、具体功能、项目亮点、技术栈等画功能结构图所必须了解的问题，组长给我进行了很详细的解答，我也对我们的项目宏观上的框架和微观上的功能有了较深的了解。

## 2022.7.8

- 正式开始着手绘制功能结构图的工作，今天主要的工作是绘制了项目的主体部分的结构图——包括图片上传和照片识别的功能。
- 其中图片上传的功能主要包括了web端和小程序，web端上传图片可以从电脑中选择，也可以上传压缩包；小程序端可以支持从手机相册中上传图片。

## 2022.7.9

- 绘制系统结构图的另外一个主要的部分——数据展示部分。
- 数据展示部分，我们的项目采用柱状图、折线图、扇形图等方式，以可视化的形式显示了已检测的零件数目、显示了累积的检测用时、显示了正常零件的占比、以及给出系统关于工业品的评价和建议。

## 2022.7.11

- 绘制系统结构图的最后一个部分：算法部分。
- 我们的项目主要采用迁移学习和VGG模型，还用到了一些特征工程的方法，并且使用了英特尔模型加速的方法对我们的算法性能进行了优化。我将这些使用的算法方法页绘制到了我们系统的功能结构图当中。

## 2022.7.12

- 下午15：00，参加由英特尔指导老师主持的最后一次的答疑会。
- 将初版结构图发给小组长，小组长给我提出了一些很好的修改建议，并且与我讨论了如何优化我们的结构图，使得图示可以更加的重点突出、美观。
- 与小组长讨论后，我将昨天做的算法部分的图示进行简化，因为我们认为作为功能结构图，应该突出的展示我们的系统可以实现的功能，而算法部分是我们开发者着重关注的东西，在结构图中可以一笔带过。
- 在Xmind中给结构树换了一种新的样式，使得结构树看起来更加的直接和美观。

## 2022.7.13

- 还剩两天时间就答辩了，项目进入收尾阶段。收尾阶段主要是需要我绘制一些图示来辅助项目总结报告的撰写和最终答辩。
- 我今天主要的工作是需要绘制一个上传图片的流程图，以直观明了地介绍我们的核心功能——上传图片以进行工业品检测。

## 2022.7.14

- 将绘制好的上传图片的流程图发给小组长，小组长提供了一些修改意见，我根据她的建议和我自己的想法对与流程图进行了一些修改，并形成最后的终版流程图，发给小组长。
- 准备7月15日的最终答辩。

## 2022.7.15

- 下午就要进行最终答辩了，今天在准备答辩的内容。
- 项目到今天就要完美收官了，这可能是最后一次更新github项目博客了，通过本次暑期实训，感觉自己收获颇丰，也有了很大的进步。
