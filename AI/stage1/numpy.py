# 导入 NumPy 库，这是 Python 中科学计算的核心库
import numpy as np

# 创建一个 3x3 的二维数组，指定数据类型为 64 位整数
array = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]], dtype=np.int64)

# 打印数组内容及各项属性
print(array)                             # 输出数组本身
print('array of type:', array.dtype)     # 数据类型（int64）
print('number of dimensions:', array.ndim)  # 维度数（2）
print('number of shape:', array.shape)   # 形状（3行 × 3列）
print('number of elements:', array.size) # 元素总数（9）

# 创建各种类型的数组用于演示
a = np.zeros((3, 3))                     # 全零数组，形状为 3×3
b = np.empty((3, 3))                     # 空数组（内容未初始化，为随机值），形状为 3×3
c = np.arange(10, 20, 2)                # 从 10 到 20（不含）步长为 2 的一维数组：[10, 12, 14, 16, 18]
d = np.arange(6).reshape(2, 3)           # 生成 0-5 的一维数组，再重塑为 2×3 的二维数组
e = np.linspace(1, 10, 6).reshape(2, 3) # 在 1 到 10 之间生成 6 个等间距的数，再重塑为 2×3

# 依次打印各数组
print(a)
print(b)
print(c)
print(d)
print(e)
