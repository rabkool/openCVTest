import cv2

# 读取图片 1代表彩色，0代表灰度图片
img = cv2.imread('rabkool.jpg', 1)

# 弹框显示
cv2.imshow('rabkool', img)

# 不加这个闪退
cv2.waitKey(0)
