# ============================================================
# pandas_learn.py —— pandas 基础学习示例（详细注释版）
#
# 本脚本演示 pandas 的两类核心数据结构：
#   1. Series（一维带标签数据，类似带索引的列表）
#   2. DataFrame（二维表格数据，类似 Excel 表格）
#
# 涵盖内容：
#   - 创建 Series
#   - 生成日期序列（date_range）
#   - 创建 DataFrame 的多种方式（随机数组、arange、字典混合类型）
#   - 查看数据类型 / 索引 / 列名 / 数值
#   - 描述性统计（describe）
#   - 转置（T）
#   - 排序（sort_index / sort_values）
#   - 索引与切片（[]、.loc、.iloc、布尔过滤）
#   - 修改与新增列（单步赋值、索引对齐）
#   - 缺失值处理（dropna / fillna / isnull）
#   - CSV 文件读取与 Markdown 导出
#   - concat 拼接多个 DataFrame（含 join / reindex）
#
# 运行方式：python pandas_learn.py
# ============================================================

# ------------------------------------------------------------
# 0. 导入库
# ------------------------------------------------------------

# 导入 pandas 并起别名 pd。
# pandas 是 Python 最常用的数据分析库，提供 Series、DataFrame
# 等数据结构，以及数据处理、清洗、统计分析等功能。
# 注意：本脚本的写法要求 pandas 0.20 以上（.ix 已被移除）。
import pandas as pd

# 导入 numpy 并起别名 np。
# numpy 是科学计算基础库，本脚本用到了：
#   np.nan            —— 缺失值（Not a Number）
#   np.random.randn() —— 生成标准正态分布随机数
import numpy as np


# ------------------------------------------------------------
# 1. Series：一维带标签数据
# ------------------------------------------------------------

# pd.Series(...) 用列表创建一维序列：
#   数据 -> [1, 2, 3, 4, 5, 6, np.nan]
#   索引 -> 未指定，pandas 自动生成从 0 开始的整数索引（0、1、...、6）
# np.nan 表示"缺失值"（Not a Number），是数据分析中常见的空值标记，
# 在输出中会显示为 NaN。
# 注意：因为混入了 np.nan（浮点型），整列数据类型会自动变为 float64。
a = pd.Series([1,2,3,4,5,6,np.nan])

# print(a) 输出结果包含两列：
#   左列是索引（index，0~6），右列是对应的数值；
#   最后一个值是 NaN（缺失值）。
# 输出大致如下：
#   0    1.0
#   1    2.0
#   ...
#   6    NaN
#   dtype: float64
print(a)


# ------------------------------------------------------------
# 2. date_range：生成连续的日期序列
# ------------------------------------------------------------

# pd.date_range 用于生成连续的时间索引：
#   start='20260811'：起始日期为 2026 年 8 月 11 日；
#   periods=6：一共生成 6 个时间点（默认按天递增）。
dates = pd.date_range(start='20260811', periods=6)

# print(dates) 将得到 2026-08-11 到 2026-08-16 共 6 天，
# 类型为 DatetimeIndex（pandas 内置的时间索引类型），
# 可直接作为 DataFrame 的行索引使用。
print(dates)


# ------------------------------------------------------------
# 3. DataFrame：二维表格数据
# ------------------------------------------------------------

# np.random.randn(6, 4) 生成 6 行 4 列、服从标准正态分布的随机数
# （均值约 0、标准差约 1）；
# pd.DataFrame(...) 把它包装成表格：
#   index=dates            行索引为前面生成的 6 个日期；
#   columns=list('ABCD')   列名为 A、B、C、D。
# 由于数据是随机数，每次运行输出的数值都会不同。
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

# print(df) 将看到一张 6 行 4 列的表格：
#   行索引是 2026-08-11 ~ 2026-08-16；
#   列名是 A、B、C、D；
#   每个单元格是一个随机浮点数。
print(df)

# np.arange(12) 生成 0~11 共 12 个连续整数的一维数组；
# .reshape((3, 4)) 将其整理成 3 行 4 列的二维数组；
# 再交给 pd.DataFrame(...) 创建表格。
# 未指定 index 和 columns 时，pandas 自动使用 0、1、2... 作为行列索引。
df1 = pd.DataFrame(np.arange(12).reshape((3,4)))

# print(df1) 将得到一张 3 行 4 列、值为 0~11 的表格：
#   行索引为 0、1、2，列名为 0、1、2、3。
print(df1)


# ------------------------------------------------------------
# 4. 用"字典 + 混合类型"方式创建 DataFrame
# ------------------------------------------------------------
# 字典的每个键（key）会成为一列，每个值（value）是该列的数据。
# 这种方式可以同时容纳多种数据类型，pandas 会按列自动推断类型。
# 本字典定义了 6 个键（A~F），对应 6 列，最终得到 4 行 6 列的表格：
#   A：标量 1.0（float），pandas 会自动"广播"填充到所有 4 行；
#   B：pd.Timestamp('20210607')，一个时间戳，演示 datetime 类型列；
#   C：pd.Series(1, index=0~3, dtype='float32')，4 个值为 1 的 float32 序列；
#   D：np.array([3]*4, dtype='int32')，4 个值为 3 的 int32 数组；
#   E：pd.Categorical(...)，分类数据，适合表示有限取值的离散变量；
#   F：字符串 'foo'，同样广播到每一行。
df2 = pd.DataFrame({'A':1.,
                'B':pd.Timestamp('20210607'),
                'C':pd.Series(1,index=list(range(4)),dtype='float32'),
                'D':np.array([3]*4,dtype='int32'),
                'E':pd.Categorical(["test","train","test","train"]),
                'F':'foo'})

# print(df2) 将输出一张 4 行 6 列的表格：
#   行索引是 0~3；
#   A 列全是 1.0，B 列全是 2021-06-07，
#   C 列全是 1.0（float32），D 列全是 3（int32），
#   E 列是 test/train 交替出现，F 列全是 'foo'。
print(df2)


# ------------------------------------------------------------
# 5. DataFrame 的常用属性
# ------------------------------------------------------------

# df2.dtypes：查看每一列的数据类型。
# 返回一个 Series：索引是列名，值是类型。
# 本例输出大致为：
#   A          float64
#   B    datetime64[ns]
#   C          float32
#   D            int32
#   E        category
#   F           object
print(df2.dtypes)

# df2.index：查看行索引。
# 本例未指定 index，默认是 RangeIndex(0, 4)，即 0、1、2、3。
print(df2.index)

# df2.columns：查看列名列表，即 ['A', 'B', 'C', 'D', 'E', 'F']。
print(df2.columns)

# df2.values：以 numpy 二维数组的形式返回 DataFrame 中的数据，
# 注意：它不包含行索引和列名，只包含纯数值。
print(df2.values)

# df2.describe()：生成描述性统计摘要，
# 对每一列统计：
#   count —— 非缺失值的数量
#   mean  —— 均值
#   std   —— 标准差
#   min   —— 最小值
#   25% / 50% / 75% —— 四分位数
#   max   —— 最大值
# 默认只统计数值型列，本示例中为 A、C、D 三列。
print(df2.describe())

# df2.T：转置（Transpose），把行列互换：
#   原来的行索引变成列名，原来的列名变成行索引。
# 对于 df2（4 行 6 列），转置后变成 6 行 4 列。
print(df2.T)


# ------------------------------------------------------------
# 6. 排序
# ------------------------------------------------------------

# df2.sort_index(axis=1, ascending=False)：按"列索引"（列名）排序。
#   axis=1：沿列方向操作，即对列名 A~F 排序；
#   ascending=False：降序，因此列会按 F、E、D、C、B、A 排列。
# 注意：排序只影响输出的顺序，不会修改 df2 本身。
print(df2.sort_index(axis=1,ascending=False))

# df2.sort_index(axis=0, ascending=False)：按"行索引"排序。
#   axis=0：沿行方向操作，即对行索引 0~3 排序；
#   ascending=False：降序，因此行会按 3、2、1、0 排列。
print(df2.sort_index(axis=0,ascending=False))

# df2.sort_values(by='E', ascending=False)：按指定"列的值"排序。
#   by='E'：根据 E 列的值排序；
#   E 是分类数据（test/train）；
#   ascending=False：降序，因此 train 行会排在 test 行前面。
print(df2.sort_values(by='E',ascending=False))


# ------------------------------------------------------------
# 7. 索引与切片：从 DataFrame 中取出需要的行和列
# ------------------------------------------------------------
# 下面演示三种主要取值方式：
#   df[...]      —— 方括号：取列，或按位置/标签对行切片；
#   .loc         —— 按"标签"选取（行索引名、列名），切片是闭区间；
#   .iloc        —— 按"位置"选取（第几行、第几列），切片左闭右开。
# 此外还有"布尔过滤"：根据条件挑选满足条件的行。

# df['A']：按列名取出一列，结果是 Series，列名 A 成为该 Series 的名字；
# df.A：等价的"属性"写法，效果相同（仅当列名是合法标识符时才可用）。
# 两者都返回 A 列的 6 个随机数，行索引仍是那 6 个日期。
print(df['A'],df.A)

# df[0:3]：方括号里传整数切片时，按"行位置"取前 3 行
#          （位置 0、1、2），等价于 df.iloc[0:3]；
# df['20260811':'20260813']：方括号里传日期字符串时，
#          pandas 会把字符串解析为行索引标签，
#          按"标签"取 2026-08-11 到 2026-08-13 这三天的行。
#          注意：标签切片是闭区间，两端都包含。
print(df[0:3],df['20260811':'20260813'])

# df.loc['20260811']：按行索引标签取"一行"，
# 返回一个 Series，索引是列名 A~D，值是当天的 4 个随机数。
print(df.loc['20260811'])

# df.loc['20260811':, ['A','B']]：按标签同时选取行和列：
#   行：从标签 '20260811' 开始一直到最后一行（'20260811': 表示"从该标签起"）；
#   列：只取 A、B 两列。
# 结果是包含 6 行 2 列的 DataFrame。
print(df.loc['20260811':,['A','B']])

# df.iloc[3:5, 1:3]：按"位置"同时选取行和列：
#   行：位置 3 和 4（第 4、5 行；切片右侧不包含位置 5）；
#   列：位置 1 和 2（第 2、3 列，即 B、C 列）。
# 结果是 2 行 2 列的 DataFrame。
print(df.iloc[3:5,1:3])

# 旧版 pandas 用 df.ix[:3,['A','C']] 做"混合索引"
# （按位置切前 3 行 + 按标签选 A、C 列），
# 但 .ix 在 pandas 0.20 之后已被移除。
# 等价写法：df.index[:3] 先取出前 3 个行标签（日期），
# 再交给 .loc 按标签同时选取行和列。
# 结果是 3 行 2 列（A、C 列）的 DataFrame。
print(df.loc[df.index[:3],['A','C']])

# df[df.A<0]：布尔过滤（条件筛选）。
#   先计算 df.A<0：对 A 列的每个值判断是否小于 0，
#   得到一个全为 True/False 的布尔 Series；
#   再把它作为行索引传入 df[...]，只保留对应位置为 True 的行。
# 结果是不固定行数的 DataFrame：A 列为负数的行保留，其余丢弃。
print(df[df.A<0])

# ------------------------------------------------------------
# 8. 修改 DataFrame 中的值与新增列
# ------------------------------------------------------------
# 修改已有单元格时统一推荐用 .iloc（按位置）或 .loc（按标签），
# 不要用"先取列再赋值"的链式写法（见下方说明）；
# 给不存在的列名直接赋值，则是"新增一列"。

# df.iloc[2,2] = 111：按"位置"定位到第 3 行第 3 列（C 列），
# 把该单元格的值改成 111。
df.iloc[2,2] = 111

# df.loc['20260811','B'] = 222：按"标签"定位到 2026-08-11 这行、B 列，
# 把该单元格的值改成 222。
df.loc['20260811','B'] = 222

# 旧写法 df.A[df.A>0] = 0 属于"链式赋值"：
#   df.A 先返回一列（中间对象），再对中间对象赋值，
# 新版 pandas（Copy-on-Write）下这永远改不到原表 df，还会报错。
# 正确写法是用 .loc 一步完成：行条件 df.A>0 选中 A 列中所有正数，
# 列名 'A' 指明要改哪一列，把这些单元格统一改为 0。
df.loc[df.A>0,'A'] = 0

# df['F'] = np.nan：给 df 新增一列 F。
# 因为 F 列原本不存在，直接对列名赋值就是在表格最右侧新建列；
# 值 np.nan 是标量，pandas 会"广播"到全部 6 行，
# 所以 F 列 6 个单元格全是 NaN（缺失值），类型自动推断为 float64。
df['F'] = np.nan

# df['E'] = pd.Series([1,2,3,4,5,6], index=pd.date_range('20260811',periods=6))：
# 再新增一列 E，值来自一个带日期的 Series（1~6）。
# 关键机制是"索引对齐"：pandas 会按行标签把该 Series 与 df 的日期索引
# 一一对应起来（2026-08-11→1、2026-08-12→2、...、2026-08-16→6），
# 所以不会出现错位；若 Series 的索引与 df 不一致，匹配不上的位置会变成 NaN。
df['E'] = pd.Series([1,2,3,4,5,6],index=pd.date_range('20260811',periods=6))

# 打印最终结果：df 此时是 6 行 6 列（A、B、C、D、E、F）。
# 可以看到之前的修改：C 列第 3 行是 111、B 列首行是 222、
# A 列原来的正数都变成了 0；E 列是 1~6；F 列全是 NaN。
print(df)

# ------------------------------------------------------------
# 9. 缺失值处理
# ------------------------------------------------------------
# 经过上一步操作后，df 的 F 列全是 NaN，因此下面演示
# pandas 处理缺失值（NaN）的三种常用方式。

# df.dropna(axis=1, how='any')：删除含缺失值的"列"。
#   axis=1：沿列方向操作，即删除"列"而不是"行"；
#   how='any'：只要该列中存在任意一个 NaN 就整列删除
#              （若改为 how='all'，则只有整列全是 NaN 才删除）。
# 本例中 F 列全是 NaN，A、B、E 等列因修改后也可能出现 NaN，
# 所以打印结果里所有"包含任一 NaN"的列都会被丢掉。
# 注意：dropna 默认返回新表，不会修改原 df。
print(df.dropna(axis=1, how='any'))

# df.fillna(value=0)：把表中所有 NaN 填充为 0。
#   value=0：指定填充值，可以是标量（所有缺失位置都填 0），
#            也可以是字典/Series（按列分别指定填充值）。
# 同样地，fillna 默认返回新表，不会修改原 df。
print(df.fillna(value=0))

# df.isnull()：逐单元格判断是否为缺失值。
# 返回一个与 df 形状相同的布尔 DataFrame：
#   缺失位置 -> True，非缺失位置 -> False。
# 它是检查缺失值最常用的方法，常与 sum() 连用统计每列缺失个数。
print(df.isnull())

# np.any(df.isnull()) == True：判断表中"是否存在任何缺失值"。
#   df.isnull() 先生成布尔表；
#   np.any(...) 只要表中存在一个 True（即一个 NaN）就返回 True；
#   再与 True 比较，结果等价于 np.any(df.isnull()) 本身。
# 本例 F 列全是 NaN，所以输出 True。
print(np.any(df.isnull()) == True)


# ------------------------------------------------------------
# 10. CSV 读取与 Markdown 导出
# ------------------------------------------------------------

# pd.read_csv('air_quality_2025.csv')：读取同目录下的 CSV 文件。
# pandas 会自动识别：首行为列名、按行解析数据、自动推断各列类型。
# 返回一个 DataFrame 并赋值给 data。
# 注意：运行脚本前必须保证该 CSV 文件与脚本在同一目录下，
#       否则会抛出 FileNotFoundError。
data = pd.read_csv('air_quality_2025.csv')

# print(data) 直接打印整张表：行数多时 pandas 会自动省略中间行，
# 只显示开头和结尾各 5 行（默认显示设置）。
print(data)

# data.to_markdown('air_quality_2025.md')：把 DataFrame 导出为
# Markdown 表格，并写入同目录下的 air_quality_2025.md 文件。
# 导出的格式便于直接粘贴到 README、文档或博客中展示。
# 注意：该功能依赖第三方库 tabulate，若未安装会报错；
# 可用 pip install tabulate 安装。
data.to_markdown('air_quality_2025.md')


# ------------------------------------------------------------
# 11. concat：沿轴拼接多个 DataFrame
# ------------------------------------------------------------

# 下面三个 df 结构完全相同（都是 3 行 4 列、列名 A~D），
# 只是数值分别是 0、1、2，用于演示最常见的"纵向拼接"。
df3 = pd.DataFrame(np.ones((3,4))*0,columns=list('ABCD'))
df4 = pd.DataFrame(np.ones((3,4))*1,columns=list('ABCD'))
df5 = pd.DataFrame(np.ones((3,4))*2,columns=list('ABCD'))

# pd.concat([...], axis=0, ignore_index=True)：纵向拼接多张表。
#   axis=0：沿行方向拼接，把 df4、df5 依次接到 df3 下方；
#   ignore_index=True：忽略原有的行索引 0~2，重新生成 0~8 的连续索引。
# 最终 res 是一张 9 行 4 列的表。
res = pd.concat([df3,df4,df5],axis=0,ignore_index=True)
print(res)

# 下面两个 df 的行索引和列名都不完全一致，用于演示 join 对齐方式：
#   df6：行索引 [1,2,3]，列 A、B、C、D；
#   df7：行索引 [2,3,4]，列 B、C、D、E。
df6 = pd.DataFrame(np.ones((3,4))*0,columns=list('ABCD'),index=[1,2,3])
df7 = pd.DataFrame(np.ones((3,4))*1,columns=list('BCDE'),index=[2,3,4])

# join='inner'：列只保留两边"都有"的（交集 B、C、D）；
#              行是纵向堆叠，全部保留，不取交集。
# 注意：ignore_index=True 会丢掉原始行索引 [1,2,3]、[2,3,4]，
#       重新编号为 0~5，因此这里看不到行索引的对齐效果。
res1 = pd.concat([df6,df7],axis=0,ignore_index=True,join='inner')
print(res1)
# join='outer'（默认值）：列保留两边"所有"的（并集 A~E），
#                        某张表没有的列自动填 NaN。
res2 = pd.concat([df6,df7],axis=0,ignore_index=True,join='outer')
print(res2)
# 旧版 pandas 曾支持 join_axes=[df6.index]，表示"拼接后只保留
# df6 的行索引 [1,2,3]"；但 pandas 2.0 起该参数已被移除，
# 直接使用会报错：concat() got an unexpected keyword argument 'join_axes'。
# 官方推荐的等价写法是"先 reindex 再拼接"：
#   df7.reindex(df6.index)：把 df7 的行索引重排成 [1,2,3]，
#       df7 中原本索引为 1、4 的行因找不到对应标签而变成 NaN；
#   然后与 df6 一起纵向拼接，得到 6 行（索引 1、2、3、1、2、3）。
res3 = pd.concat([df6, df7.reindex(df6.index)], axis=0)
print(res3)

# df.join(s)：把 Series 横向并到 DataFrame 末尾，成为新的一列。
# 使用时有两点必须注意：
#   1. Series 必须有 name —— 它将成为新列的列名；
#      缺 name 会直接报错：ValueError: Other Series must have a name。
#   2. join 是按"行索引"对齐的：df6 的行索引是 [1,2,3]，
#      下面 s1 的 index 是 [1,2,3,4]：其中 1、2、3 能与 df6 对上，
#      E 列得到对应值 1、2、3；索引 4 在 df6 中不存在，
#      加上 join 默认 how='left'（只保留左侧 df6 的行索引），
#      所以 s1 索引为 4 的那一行会被丢弃。
s1 = pd.Series([1,2,3,4],index=[1,2,3,4],name='E')
print(df6.join(s1))

# 新行：构造一个只有一行的 DataFrame，再拼接到 df6 末尾。
# 注意：不能写 pd.DataFrame([9,8,7,6], ...) ——
# 单层列表 [9,8,7,6] 会被 pandas 当成"一列数据"（4 行 1 列），
# 与 columns=list('ABCD')（4 列）、index=[4]（1 行）冲突，会报错：
#   ValueError: Shape of passed values is (4, 1), indices imply (1, 4)
# 要表示"一行 4 列"，数据必须是"列表的列表"：
#   [[9,8,7,6]]：外层 1 个元素 = 1 行，内层 4 个元素 = 4 列；
# columns=list('ABCD')：给这 4 列分别命名 A、B、C、D；
# index=[4]：给新行指定行索引 4，不与 df6 现有的 1、2、3 重复。
new_row = pd.DataFrame([[9,8,7,6]],columns=list('ABCD'),index=[4])

# 另一种等价写法：用"字典列表"，键直接写成列名，更直观：
# new_row = pd.DataFrame([{'A':9,'B':8,'C':7,'D':6}],index=[4])

# pd.concat([df6, new_row])：把新行纵向接到 df6 末尾。
# 这里没有写 ignore_index=True，所以行索引保持原样：1、2、3、4；
# new_row 的索引 [4] 不与 df6 现有索引冲突，拼接结果干净。
# 注意：concat 返回的是新表，必须用 df6 = ... 接住，原 df6 本身不变。
df6 = pd.concat([df6, new_row])

# print(df6) 输出 4 行 4 列：
#   前三行是原来的 0.0（行索引 1、2、3），
#   最后一行是新增的 9.0 / 8.0 / 7.0 / 6.0（行索引 4）。
print(df6)
