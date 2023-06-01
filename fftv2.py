import math

PI=math.pi

'''
  按时间抽选的基-2快速傅里叶变换（n点）
  需要传入list<Complex>
'''
def fft_dit2(seq: list):
  # 检查是否为2^L点FFT
  N = len(seq)
  if int(math.log2(N)) - math.log2(N) != 0:
    raise ValueError('[fft_dit2] Not 2^L long sequence.')

  # 输入数据倒位序处理
  new_index = [0]
  J = 0 # J为倒位序
  for i in range(N - 1): # i为当前数
    mask = N // 2
    while mask <= J: # J的最高位为1
      J -= mask # J的最高位置0
      mask = mask >> 1 # 准备检测下一位
    J += mask # 首个非1位置1
    new_index.append(int(J))
  for i in range(N):
    if new_index[i] <= i:
      continue # 无需对调
    seq[i], seq[new_index[i]] = seq[new_index[i]], seq[i] # 交换

  # 计算所有需要的旋转因子WN^k（k在0~N/2-1)
  # 一种优化策略是使用递推式WN(k+1) = WN(k) * e^(-j 2PI/N)计算
  WNk = []
  two_pi_div_N = 2 * PI / N # 避免多次计算
  for k in range(N // 2):
    # WN^k = cos(2kPI/N) - j sin(2kPI/N)
    WNk.append(Complex(math.cos(two_pi_div_N * k), math.sin(two_pi_div_N * -k)))

  # 蝶形运算
  L = int(math.log2(N)) # 蝶形结层数
  for m in range(1, L + 1): # m为当前层数，从1开始
    # 见课本P219表4.1
    distance = 2 ** (m - 1) # 对偶结点距离，也是该层不同旋转因子的数量
    for k in range(distance): # 以结合的旋转因子为循环标准，每一轮就算掉该旋转因子对应的2^(L-m)个结
      r = k * 2 ** (L - m) # 该旋转因子对应的r
      for j in range(k, N, 2 ** m): # 2^m为每组旋转因子对应的分组的下标差
        right = seq[j + distance] * WNk[r]
        t1 = seq[j] + right; t2 = seq[j] - right
        seq[j] = t1; seq[j + distance] = t2

  return seq

'''
  快速傅里叶变换的反变换
  需要传入list<Complex>
'''
def ifft(seq: list):
  # 检查是否为2^L点序列
  N = len(seq)
  if int(math.log2(N)) - math.log2(N) != 0:
    raise ValueError('[ifft] Not 2^L long sequence.')

  # 先对X(k)取共轭
  seq = list(map(lambda x : x.conjugate(), seq))
  # 再次利用FFT
  seq = fft_dit2(seq)
  # 再取共轭
  seq = map(lambda x : x.conjugate(), seq)
  # 最后除以N
  seq = map(lambda x : x * Complex(1 / N, 0), seq)

  return list(seq)




'''
  实用函数，打印FFT结果
'''
def print_fft_result(seq: list):
  toprint = '[\n'
  modder = 0
  for cplx in seq:
    toprint += str(cplx)
    toprint += '\t\t' if modder != 3 else '\n'
    modder += 1
    modder %= 4
  toprint += ']'
  return toprint

'''
  实用函数，给实序列补0到指定长度，可用于采样点数小于FFT点数
'''
def add_zero_to_length(seq: list, n: int):
  if len(seq) == n:
    return seq
  # 如果点数不足，把seq补到n点
  if len(seq) > n:
    raise ValueError('[add_zero_to_length] n < len(seq).')
  if len(seq) < n:
    res = [*seq]
    while (len(res) < n):
      res.append(0)
  return res
