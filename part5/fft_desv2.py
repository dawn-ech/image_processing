import numpy as np
import matplotlib.pyplot as plt


N = 64

def get_coords(N, length):
    gap = length / (N//4)
    contour = []
    for i in range(N):
        if i < N//4:
            x = gap * i
            y = 0
        elif i < N//2:
            x = gap * (N//4)
            y = gap * (i-N//4)
        elif i < N//4*3:
            x = gap * (N//4 - (i-N//2))
            y = gap * (N//4)
        else:
            x = 0
            y = gap * (N//4 - (i-N//4*3))

        # x = gap * i if i < N/2 else length - gap * (N - i - 1)  # 水平方向坐标
        # y = gap * i if i < N/2 else length - gap * (N - i - 1)  # 垂直方向坐标
        contour.append((x, y))

    return contour

contour = get_coords(N, 1)
points = np.array(contour)
edge_points = np.zeros((points.shape[0],), dtype=complex)
edge_points.real = points[:, 0]
edge_points.imag = points[:, 1]


from fft import fft, ifft

a_k  = fft(edge_points)
#print(a_k)

M = 48
for i in range(M, len(a_k)):
    a_k[i] = 0

ori = ifft(a_k)

#print(ori)

x_coords, y_coords = zip(*contour)
# 绘制轮廓点
#plt.plot(x_coords, y_coords, marker='o')
plt.subplot(121)
plt.scatter(x_coords, y_coords, marker='o')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Square Contour')
plt.axis('equal')  # 设置坐标轴比例相等
#plt.show()


ori = np.array(ori)
x_coords = ori.real
y_coords = ori.imag
# 绘制轮廓点
#plt.plot(x_coords, y_coords, marker='o')
plt.subplot(122)
plt.scatter(x_coords, y_coords, marker='o')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Square Contour')
plt.axis('equal')  # 设置坐标轴比例相等
plt.show()