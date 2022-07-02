# 开发日志-徐熙

## 6月22日

+ 进行第一次会议，认识需求，定义问题。提出使用迁移学习方法（transfer learning）完成模型训练

## 6月23日

+ 学习论文https://arxiv.org/abs/1512.04150，尝试使用VGG-16 + Classification head (Global Average Polling）模型

## 6月24日

+ 定义dataloader, helper, model三个模块的需求，以及Pytorch相应代码学习

## 6月25日

+ 完成model模块代码，完成定义模型

## 6月26日

+ 完成dataloader，helper模块代码，实现训练pipeline

## 6月28日

+ 完成training模块代码，并使用原始数据集进行第一次训练得到如下结果：
  Loss = 0.1969, Accuracy = 0.8536
  Epoch 2/10: Loss = 0.1010, Accuracy = 0.9036
  Epoch 3/10: Loss = 0.0718, Accuracy = 0.9339
  Epoch 4/10: Loss = 0.0355, Accuracy = 0.9750
  Epoch 5/10: Loss = 0.0309, Accuracy = 0.9857
  Early Stopping

​	   Accuracy: 0.9362
​	   Balanced Accuracy: 0.7750

## 6月29日

+ 使用数据增强后的数据集dataplus进行训练，并调参得到：
  Accuracy: 0.9857
  Balanced Accuracy: 0.9927

## 6月30日

+ 组会分享工作进程并与组员沟通下一步工作

## 7月1日

+ Deploy模型到web端，完成transform_image; get_prediction两个方法

## 7月2日

+ 学习explainable AI，实现缺陷自动标注功能