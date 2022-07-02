"""
加载defect_product中的数据并对图像进行旋转、编号等操作
"""
import os
from PIL import Image  # 常用的图像处理的库
import cv2
import numpy as np

# 从路径中读取图片
ROOT_DATA = r'C:\Users\FR\PycharmProjects\pythonProject\summerProject\data\defect_product'
# 旋转后的图像记录
ROOT_SPLITS = r'C:\Users\FR\PycharmProjects\pythonProject\summerProject\data'
IMG_CACHE = {}  # 保存图像数据，路径：格式等信息


class Defect_Prpduct(object):
    def __init__(self, setname):
        # .txt中的每行表示：种类/编号/旋转的角度,作为数据的类别
        splits = os.path.join(ROOT_SPLITS, setname + ".txt")

        # 定义数据集类别
        with open(splits) as f:
            self.classes = f.read().splitlines()

        # 读取全部图像,图像名称、类别、目录、旋转情况
        self.all_images = find_images(os.path.join(ROOT_DATA), self.classes)

        # 给图像标注下标
        self.inx_classses = index_classes(self.all_images)

        # paths表示不同图像的存储路径，包括旋转
        paths = [self.get_path_label(pl) for pl in range(len(self))]
        # paths = [self.get_path_label(pl) for pl in range(4)]

        self.input = map(load_image, paths, range(len(paths)))  # path 和 range(len(paths))按照load_image的规则进行映射
        self.input = list(self.input)
        print(type(self.input[0]))

    def __len__(self):
        return len(self.all_images)

    # 得到旋转后图像的路径
    def get_path_label(self, index):
        filename = self.all_images[index][0]
        rot = self.all_images[index][-1]
        img = str.join(os.sep, [self.all_images[index][2], filename]) + rot
        return img


# 找到全部图片
def find_images(path, classes):
    res = []
    rots = [os.sep + 'rot000', os.sep + 'rot090', os.sep + 'rot180', os.sep + 'rot270']
    for file in os.listdir(path):
        r = file.split('.')
        label = r[0]
        for rot in rots:
            if label + rot in classes and file.endswith('.JPG'):
                res.extend([(file, label, path, rot)])
    return res


# 给每个图片从0开始标号
def index_classes(images):
    index = {}
    for image in images:
        if image[1] + image[-1] not in index:
            index[image[1] + image[-1]] = len(index)
    return index


# 加载数据的规则：旋转、放缩等
def load_image(path, index):
    path, rot = path.split(os.sep + 'rot')
    r = path.split(os.sep)
    if path in IMG_CACHE:
        input = IMG_CACHE[path]
    else:
        input = Image.open(path)
        IMG_CACHE[path] = input
    input = input.rotate(float(rot))  # rotate对图像进行旋转
    # input.show()
    cv_input = cv2.cvtColor(np.asarray(input), cv2.COLOR_RGB2BGR)
    # 保存cv_input
    cv2.imwrite(r"C:\Users\FR\PycharmProjects\pythonProject\summerProject\dataplus"+os.sep+str(r[-1][0:3]+'-rot'+rot)+'.JPG',cv_input)

    if rot == '000':
        imgFlip1 = cv2.flip(cv_input, 0)  # 垂直翻转
        imgFlip2 = cv2.flip(cv_input, 1)  # 水平翻转
        # cv2.imshow('shuiping0', imgFlip1)
        # cv2.imshow('shuiping1', imgFlip2)
        cv2.imwrite(r"C:\Users\FR\PycharmProjects\pythonProject\summerProject\dataplus" + os.sep + str(
            r[-1][0:3] + '-flipv') + '.JPG', imgFlip1)
        cv2.imwrite(r"C:\Users\FR\PycharmProjects\pythonProject\summerProject\dataplus" + os.sep + str(
            r[-1][0:3] + '-fliph') + '.JPG', imgFlip2)

    return input


if __name__ == "__main__":
    test_dataset = Defect_Prpduct('data_rot')

    # 把图像转为opencv2
    # test0 = cv2.cvtColor(np.asarray(test_dataset.input[0]), cv2.COLOR_RGB2BGR)
    # cv2.imshow("OpenCV0", test0)
    # cv2.waitKey()
    # print(type(test0)) # numpy.ndarray
    # cv2.imwrite("/home/1.jpg")  # 不过应该不需要保存把..
