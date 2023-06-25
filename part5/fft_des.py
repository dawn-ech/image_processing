import numpy as np
import matplotlib.pyplot as plt

N = 64

def get_coords(N, length):
    gap = length / (N - 1)
    contour = []
    for i in range(N):
        x = gap * i if i < N/2 else length - gap * (N - i - 1)  # 水平方向坐标
        y = gap * i if i < N/2 else length - gap * (N - i - 1)  # 垂直方向坐标
        contour.append((x, y))

    return contour

contour = get_coords(N, 1)
x_coords, y_coords = zip(*contour)
# 绘制轮廓点
plt.plot(x_coords, y_coords, marker='o')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Square Contour')
plt.axis('equal')  # 设置坐标轴比例相等
plt.show()