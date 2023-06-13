import cv2
import matplotlib.pyplot as plt

# 加载灰度图像
image = cv2.imread('gray.jpg', 0)


def exp(x, gamma=0.5):
    return x**gamma
    pass


# 创建输出图像
output = [[exp(pixel) for pixel in row] for row in image]

# 显示原始图像和均衡化后的图像
plt.subplot(121)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(122)
plt.imshow(output, cmap='gray')
plt.title('EXP Image')
plt.axis('off')

plt.show()
