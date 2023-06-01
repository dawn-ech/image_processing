import numpy as np
from numpy import arange, sin, pi, cos
import math
import cmath
import matplotlib.pyplot as plt

test_img = np.zeros((128, 128))

test_img[63:67, 63:67] = 1

# plt.imshow(test_img, cmap='gray')
# plt.show()


def DFT_2D(img):
    N, M = img.shape
    assert N == M
    F1 = np.apply_along_axis(DFT_1D, 1, img)
    F2 = np.apply_along_axis(DFT_1D, 0, F1)
    return F2
    return F2 / (N * N)


    pass


# 对向量进行1D傅里叶变换
def DFT_1D(vec):
    '''
        Xk = \sum x(n)*exp(-j*2*pi/N*nk)
    '''
    N = len(vec)
    F = []
    for k in range(N):
        r = 0
        for n in range(N):
            r += vec[n] * cmath.exp(-1j*2*pi*n*k/N)
        F.append(r/N)
    return np.array(F)

def FFT_1D(vec):
    pass

a = np.array([2,3,4,4])
print(DFT_1D(a))

test_img = np.array(
    [
        [1, 5, 6],
        [8, 9, 16],
        [5, 2, 33]
    ]
)

fft = DFT_2D(test_img)
print(fft*9)

plt.imshow(fft, cmap='gray')
# plt.show()