import cv2
import matplotlib.pyplot as plt

# 加载灰度图像
image = cv2.imread('gray.jpg', 0)

# 计算灰度级别的像素频率
freqs = [0] * 256
for row in image:
    for idx in row:
        freqs[idx] += 1

s = [0] * 256
s[0] = freqs[0]

# 计算累积概率
for i in range(1, 256):
    s[i] = s[i-1] + freqs[i]

s_max = s[-1]

# 计算变换后的灰度级
level2 = [int(256 * x / s_max)-1 for x in s]

# 创建输出图像
output = [[level2[pixel] for pixel in row] for row in image]

# 显示原始图像和均衡化后的图像
plt.subplot(121)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(122)
plt.imshow(output, cmap='gray')
plt.title('Histogram Equalized Image')
plt.axis('off')

plt.show()
