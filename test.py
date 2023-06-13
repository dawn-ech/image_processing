import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取图像
image = cv2.imread('1.jpg', 0)

image = np.zeros((128, 128))

image[63:67, 63:67] = 1

# 执行傅里叶变换
f = np.fft.fft2(image)
f_shift = np.fft.fftshift(f)
magnitude_spectrum = np.abs(f_shift)
#magnitude_spectrum = 20 * np.log(np.abs(f_shift))

# 显示原始图像
plt.subplot(121), plt.imshow(image, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])

# 显示傅里叶频谱
plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])

plt.show()
