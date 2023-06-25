import cmath

def fft(x):
    N = len(x)
    if N <= 1:
        return x
    
    # 确保序列长度为2的幂次方
    # k = log(N)
    k = N.bit_length() - 1
    if N != 2**k:
        raise ValueError("序列长度必须是2的幂次方")
    
    # 位重排
    x = bit_reverse(x)
    
    # 迭代计算, 从1到log(N)
    for s in range(1, k + 1):
        # m为一个计算周期, m//2 为对偶节点距离
        m = 2**s
        omega_m = cmath.exp(-2j * cmath.pi / m)
        for k in range(0, N, m):
            omega = 1
            for j in range(0, m // 2):
                # k+j和k+j+m//2为对偶节点
                t = omega * x[k + j + m // 2]
                u = x[k + j]
                x[k + j] = u + t
                x[k + j + m // 2] = u - t
                omega *= omega_m
    
    return x

def bit_reverse(x):
    N = len(x)
    # 输入向量长度N为2的幂次时，每个位置2进制长度为N.length()-1
    n_bits = N.bit_length() - 1
    #print(n_bits)
    reversed_indices = [0] * N
    for i in range(N):
        # 设置b的长度为n_bits，从0到N-1遍历每个数，并且反转
        b = '{:0{width}b}'.format(i, width=n_bits)[::-1]
        #print(b)
        reversed_indices[i] = int(b, 2)
    result = [x[i] for i in reversed_indices]
    return result

def ifft(x):
    N = len(x)
    if N <= 1:
        return x
    
    # 确保序列长度为2的幂次方
    # k = log(N)
    k = N.bit_length() - 1
    if N != 2**k:
        raise ValueError("序列长度必须是2的幂次方")
    x = list(map(lambda i : i.conjugate(), x))
    x = fft(x)
    x = list(map(lambda i : i.conjugate(), x))
    x = list(map(lambda i : i / N, x))
    return x

import numpy as np
import matplotlib.pyplot as plt

def DFT_2D(img):
    N, M = img.shape
    assert N == M
    F1 = np.apply_along_axis(fft, 1, img)
    F2 = np.apply_along_axis(fft, 0, F1)
    return F2


def shift(img):
    # 获取频谱图像的大小和中心位置
    height, width = img.shape
    center_y, center_x = height // 2, width // 2

    # 计算平移量
    shift_y = center_y
    shift_x = center_x

    # 平移频谱图像
    shifted_spectrum = np.roll(img, shift_y, axis=0)
    shifted_spectrum = np.roll(shifted_spectrum, shift_x, axis=1)

    return shifted_spectrum
