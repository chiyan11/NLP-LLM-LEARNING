# ============================================================
# pandas_learn.py —— pandas 基础学习示例
#
# 本脚本演示 pandas 的两类核心数据结构：
#   1. Series（一维带标签数据，类似带索引的列表）
#   2. DataFrame（二维表格数据，类似 Excel 表格）
#
# 涵盖内容：创建 Series、生成日期序列、创建 DataFrame 的多种方式、
# 查看数据类型/索引/列名/数值、描述性统计、转置以及排序等常用操作。
# ============================================================

# ------------------------------------------------------------
# 0. 导入库
# ------------------------------------------------------------

# 导入 pandas 并起别名 pd。
# pandas 是 Python 最常用的数据分析库，提供 Series、DataFrame
# 等数据结构，以及数据处理、清洗、统计分析等功能。
import pandas as pd

# 导入 numpy 并起别名 np。
# numpy 是科学计算基础库，本脚本用到了：
#   np.nan            —— 缺失值（Not a Number）
#   np.random.randn() —— 生成标准正态分布随机数
import numpy as np


# ------------------------------------------------------------
# 1. Series：一维带标签数据
# ------------------------------------------------------------

# 用列表 [1,2,3,4,5,6,np.nan] 创建 Series。
# 不指定索引时，pandas 会自动生成从 0 开始的整数索引。
# np.nan 表示"缺失值"，是数据分析中常见的空值标记。
a = pd.Series([1,2,3,4,5,6,np.nan])

# 打印 Series：输出结果包含两列，
# 左列是索引（index），右列是数值；缺失值显示为 NaN。
print(a)


# ------------------------------------------------------------
# 2. date_range：生成连续的日期序列
# ------------------------------------------------------------

# date_range 用于生成时间索引：
#   start='20260811'：指定起始日期为 2026 年 8 月 11 日；
#   periods=6：共生成 6 个时间点（默认按天递增）。
dates = pd.date_range(start='20260811', periods=6)

# 打印日期序列，将得到 2026-08-11 到 2026-08-16 共 6 天，
# 类型为 DatetimeIndex，可直接作为 DataFrame 的行索引。
print(dates)


# ------------------------------------------------------------
# 3. DataFrame：二维表格数据
# ------------------------------------------------------------

# np.random.randn(6,4) 生成 6 行 4 列、服从标准正态分布的随机数，
# 再用它创建 DataFrame：
#   index=dates            行索引为前面生成的 6 个日期；
#   columns=list('ABCD')   列名为 A、B、C、D。
# 由于是随机数，每次运行输出的数值都会不同。
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

# 打印该 DataFrame，将看到一张带日期行索引、字母列名的表格。
print(df)

# np.arange(12) 生成 0~11 共 12 个连续整数，
# .reshape((3,4)) 将其整理成 3 行 4 列的二维数组，再创建 DataFrame。
# 未指定 index 和 columns 时，pandas 自动使用 0、1、2... 作为行列索引。
df1 = pd.DataFrame(np.arange(12).reshape((3,4)))

# 打印 df1，将得到一张 3 行 4 列、值为 0~11 的表格。
print(df1)


# ------------------------------------------------------------
# 4. 用"字典 + 混合类型"方式创建 DataFrame
# ------------------------------------------------------------
# 字典的每个键（key）会成为一列，每个值（value）是该列的数据。
# 这种方式可以同时容纳多种数据类型，pandas 会按列自动推断类型。
df2 = pd.DataFrame({'A':1.,
                'B':pd.Timestamp('20210607'),
                'C':pd.Series(1,index=list(range(4)),dtype='float32'),
                'D':np.array([3]*4,dtype='int32'),
                'E':pd.Categorical(["test","train","test","train"]),
                'F':'foo'})

# 各列含义说明：
#   A：标量 1.0（浮点数），pandas 会自动广播填充到所有行；
#   B：时间戳 2021-06-07，演示 datetime 类型列；
#   C：Series，索引 0~3 共 4 个元素，值全为 1，类型 float32；
#   D：numpy 数组 [3,3,3,3]，类型 int32；
#   E：分类数据（Categorical），适合表示有限取值的离散变量；
#   F：字符串 'foo'，同样广播到每一行。

# 打印 df2，将得到一张 4 行 6 列的表格，各列数据类型不同。
print(df2)


# ------------------------------------------------------------
# 5. DataFrame 的常用属性
# ------------------------------------------------------------

# dtypes：查看每一列的数据类型
# （如 float64、datetime64[ns]、float32、int32、category、object）。
print(df2.dtypes)

# index：查看行索引（默认是 RangeIndex，即 0、1、2、3）。
print(df2.index)

# columns：查看列名列表（['A','B','C','D','E','F']）。
print(df2.columns)

# values：以 numpy 二维数组的形式返回 DataFrame 中的数据，
# 注意它不包含索引和列名，只包含纯数值。
print(df2.values)

# describe()：生成描述性统计摘要，
# 包括每列的数量（count）、均值（mean）、标准差（std）、
# 最小值（min）、四分位数（25%/50%/75%）和最大值（max）。
# 默认只统计数值型列（本示例中为 A、C、D）。
print(df2.describe())

# 转置（Transpose）：把行列互换，行索引变列名、列名变行索引。
# 对于 df2，转置后原来的 4 行 6 列会变成 6 行 4 列。
print(df2.T)


# ------------------------------------------------------------
# 6. 排序
# ------------------------------------------------------------

# sort_index(axis=1, ascending=False)：按"列索引"排序。
# axis=1 表示沿列方向，即对列名 A~F 排序；
# ascending=False 表示降序，列会按 F、E、D、C、B、A 排列。
print(df2.sort_index(axis=1,ascending=False))

# sort_index(axis=0, ascending=False)：按"行索引"排序。
# axis=0 表示沿行方向，即对行索引 0~3 排序；
# ascending=False 表示降序，行会按 3、2、1、0 排列。
print(df2.sort_index(axis=0,ascending=False))

# sort_values(by='E', ascending=False)：按指定"列的值"排序。
# by='E' 表示根据 E 列的值排序；E 是分类数据（test/train），
# ascending=False 表示降序，因此 train 行会排在 test 行前面。
print(df2.sort_values(by='E',ascending=False))
