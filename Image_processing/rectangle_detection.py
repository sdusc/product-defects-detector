import cv2

rec = []

# 定义形状检测函数
def ShapeDetection(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # 寻找轮廓点
    for obj in contours:
        area = cv2.contourArea(obj)  # 计算轮廓内区域的面积
        # cv2.drawContours(imgContour, obj, -1, (255, 0, 0), 4)  # 绘制轮廓线
        perimeter = cv2.arcLength(obj, True)  # 计算轮廓周长
        approx = cv2.approxPolyDP(obj, 0.02 * perimeter, True)  # 获取轮廓角点坐标
        # CornerNum = len(approx)  # 轮廓角点的数量
        x, y, w, h = cv2.boundingRect(approx)  # 获取坐标值和宽度、高度

        # 轮廓对象分类
        if area < 2000 and area > 300:
            rec.append([x, y, w, h, area])
            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 0, 255), 0)  # 绘制边界框

    print(rec)


if __name__ == "__main__":
    path = '081.JPG'
    img = cv2.imread(path)
    imgContour = img.copy()

    imgGray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)  # 转灰度图
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)  # 高斯模糊
    imgCanny = cv2.Canny(imgBlur, 60, 60)  # Canny算子边缘检测
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    ret, binary = cv2.threshold(imgCanny, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    ret1 = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel, iterations=5)  # 闭操作
    ret2 = cv2.morphologyEx(ret1, cv2.MORPH_OPEN, kernel, iterations=5)  # 开操作
    ShapeDetection(ret2)  # 形状检测

    a = len(rec)
    print(a)
    if a >= 4:
        print('非缺陷图片')
    else:
        print("缺陷图片")

    # cv2.imshow("Original img", img)
    # cv2.imshow("imgGray", imgGray)
    # cv2.imshow("imgBlur", imgBlur)
    # cv2.imshow("imgCanny", imgCanny)
    # cv2.imshow('ret2', ret2)
    cv2.imshow("shape Detection", imgContour)

    cv2.waitKey(0)
