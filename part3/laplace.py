import cv2
import matplotlib.pyplot as plt
import numpy as np

# 加载灰度图像
image = cv2.imread('shapen_image.jpg', 0)

window_size = 3

# 获取图像的行数和列数
H, W = image.shape

# 预处理，给图像padding
pad = window_size // 2

img = np.zeros((H + pad * 2, W + pad * 2), dtype=np.uint8)

img[pad: H + pad, pad: W + pad] = image.copy()

# 创建输出图像
output = [[0] * W for _ in range(H)]

Laplace = [
    [0, -1, 0],
    [-1, 4, -1],
    [0, -1, 0]
]
Laplace = np.array(Laplace)

gaussian = [
    [1, 2, 1],
    [2, 4, 2],
    [1, 2, 1]
]

gaussian = np.array(gaussian)/16

# # 高斯滤波
# for i in range(H):
#     for j in range(W):
#         res = np.sum(gaussian * img[i:i+window_size,j:j+window_size])
#         output[i][j] = res

# img[pad: H + pad, pad: W + pad] = output.copy()

# 遍历图像的每个像素
for i in range(H):
    for j in range(W):
        res = np.sum(Laplace * img[i:i+window_size,j:j+window_size])
        output[i][j] = image[i][j] + res
        #output[i][j] = res

output = np.clip(output, 0, 255)
output = (output - np.min(output)) / (np.max(output) - np.min(output))
#print(output)


# 显示原始图像和均衡化后的图像
plt.subplot(121)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(122)
plt.imshow(output, cmap='gray')
plt.title('Laplace Image')
plt.axis('off')

plt.show()
