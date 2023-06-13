import cv2
import matplotlib.pyplot as plt

# 加载灰度图像
image = cv2.imread('gray.jpg', 0)

window_size = 3

print(image.shape)

# 获取图像的行数和列数
H, W = image.shape


# 定义噪声密度（示例中使用0.02，即2%的像素被设置为椒盐噪声）
noise_density = 0.02

# 计算需要添加噪声的像素数量
num_noise_pixels = int(H * W * noise_density)

import random
# 随机选择要添加噪声的像素位置，并将其设置为白色或黑色
for _ in range(num_noise_pixels):
    x = random.randint(0, W - 1)
    y = random.randint(0, H - 1)
    color = random.randint(0, 1) * 255
    image[y, x] = (color)

# 创建输出图像
output = [[0] * W for _ in range(H)]

# 遍历图像的每个像素
for i in range(H):
    for j in range(W):
        start_y = max(0, i - window_size//2)
        start_x = max(0, j - window_size//2)

        end_y = min(H, i + window_size//2 + 1)
        end_x = min(W, j + window_size//2 + 1)


        # 获取邻域
        neighborhood = image[start_y: end_y, start_x: end_x]

        neighborhood = [i for item in neighborhood for i in item]


        # 将邻域像素排序并取中值作为当前像素的值
        neighborhood.sort()
        #print(neighborhood[len(neighborhood) // 2])
        #assert False
        output[i][j] = neighborhood[len(neighborhood) // 2]

#print(output)


# 显示原始图像和均衡化后的图像
plt.subplot(121)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(122)
plt.imshow(output, cmap='gray')
plt.title('Mid Image')
plt.axis('off')

plt.show()
