import cv2

img = cv2.imread('sora.jpg')
img = cv2.resize(img, (1920, 1920), interpolation=cv2.INTER_LANCZOS4)

'''
cv2.imread
flags>0时表示以彩色方式读入图片
flags=0时表示以灰度图方式读入图片
flags<0时表示以图片的本来的格式读入图片

interpolation - 插值方法。共有5种：
１）INTER_NEAREST - 最近邻插值法
２）INTER_LINEAR - 双线性插值法（默认）
３）INTER_AREA - 基于局部像素的重采样（resampling using pixel area relation）。对于图像抽取（image decimation）来说，这可能是一个更好的方法。但如果是放大图像时，它和最近邻法的效果类似。
４）INTER_CUBIC - 基于4x4像素邻域的3次插值法
５）INTER_LANCZOS4 - 基于8x8像素邻域的Lanczos插值
'''
# 弹框显示
cv2.imshow('rabkool', img)

# 不加这个闪退
cv2.waitKey(0)