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

# 导入 matplotlib 的 pyplot 模块并起别名 plt。
# matplotlib 是 Python 最常用的绘图库；pyplot 提供了类似 MATLAB 风格的
# 画图接口（plot、scatter、show 等函数）。
# 本脚本最后一部分会用 plt 画折线图、散点图并弹出窗口显示；
# 如果只做数据分析、不需要绘图，可以删除这一行。
import matplotlib.pyplot as plt

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
#   periods=6：一共生成 6 个时间点；
#   freq 未指定：默认 'D'（按天递增）。
# 也可以通过 freq 参数改变频率，例如：
#   freq='H'   按小时     freq='B'   仅工作日
#   freq='W'   按周       freq='MS'  按月首
#   freq='ME'  按月（月末）
# start、end、periods、freq 四个参数中，start 与 end 可以组合，
# 或 start 与 periods 组合，通常无需全部指定。
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
# 若表中含有 datetime、字符串等混合类型，返回的数组 dtype 是 object，
# 但每个元素仍保留各自原来的类型。
# pandas 官方新推荐写法是 df2.to_numpy()，与 .values 语义完全一致。
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
# 常用可选参数：
#   include='all'     —— 把字符串、时间等非数值列也纳入统计；
#   percentiles=[...] —— 自定义分位数（默认 [0.25, 0.5, 0.75]）。
# 对非数值列，describe 会统计 count、unique（不同值个数）、
# top（出现最多的值）、freq（最高频值的出现次数）。
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
# 多条件筛选时用 &（与）、|（或）连接，且每个条件都要加括号，例如：
#   df[(df.A < 0) & (df.B > 0)]  同时满足两个条件的行
# 注意不能写 and/or：那是对单个布尔值做逻辑运算，会直接报错。
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
# 其他常用参数：
#   thresh=n —— 只保留"非缺失值至少 n 个"的行/列；
#   subset=['A'] —— 只根据指定列是否缺失来判断；
#   inplace=True —— 原地修改 df（默认 False，返回新表）。
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
# 常用可选参数：
#   sep=','        —— 字段分隔符，默认逗号；
#   header=0       —— 用第 0 行做列名（None 表示文件没有列名行）；
#   names=[...]    —— 手动指定列名；
#   index_col=0    —— 把第 0 列当作行索引，而不是普通数据列；
#   encoding='gbk' —— 含中文的 CSV 常需显式指定 gbk 或 utf-8 编码；
#   skiprows=n     —— 读取前先跳过开头 n 行。
data = pd.read_csv('air_quality_2025.csv')

# print(data) 直接打印整张表：行数多时 pandas 会自动省略中间行，
# 只显示开头和结尾各 5 行（默认显示设置）。
print(data)

# data.to_markdown('air_quality_2025.md')：把 DataFrame 导出为
# Markdown 表格，并写入同目录下的 air_quality_2025.md 文件。
# 导出的格式便于直接粘贴到 README、文档或博客中展示。
# 注意：该功能依赖第三方库 tabulate，若未安装会报错；
# 可用 pip install tabulate 安装。
# 常用可选参数：
#   index=False —— 导出时不带行索引列（默认会带上 0、1、2... 的索引列）；
#   tablefmt='github' —— 表格样式，默认 pipe 风格。
# 若不写文件名，直接 data.to_markdown() 会返回表格字符串而不写文件。
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

# ------------------------------------------------------------
# 12. merge：按"键"横向合并两张表（类似 SQL 的 JOIN）
# ------------------------------------------------------------
# merge 与 concat 的区别：
#   concat 是简单地把表"上下（或左右）堆叠"；
#   merge 则是按某个或某几个"键列"的值进行匹配，再把两边的列拼到一起，
#   概念上等价于数据库的 INNER JOIN / LEFT JOIN / OUTER JOIN 等。

# 准备两张最简单的表，都用 key 列作为关联键：
#   left  左表：key、A、B 三列；
#   right 右表：key、C、D 三列。
left = pd.DataFrame({'key':['K1','K2','K3','K4'],'A':['A1','A2','A3','A4'],'B':['B1','B2','B3','B4']})
right = pd.DataFrame({'key':['K1','K2','K3','K4'],'C':['C1','C2','C3','C4'],'D':['D1','D2','D3','D4']})

# print(left) / print(right)：先分别查看左右两张表，确认结构。
print(left)
print(right)

# pd.merge(left, right, on='key')：
#   on='key'：指定用 key 列作为连接键；
#   how 未写，默认 'inner'（内连接），即只保留两边 key 都能匹配上的行。
# 两张表的 key 都是 K1~K4 且一一对应，因此结果是 4 行 5 列：
#   key、A、B（来自左表）+ C、D（来自右表）。
# 如果某一方缺少某个 key，对应行会被直接丢弃。
res4 = pd.merge(left,right,on='key')
print(res4)

# 多键连接：当单列不足以唯一标识一行时，用多个列组成"联合键"。
# 只有当 key1、key2 两列的值同时相等时，才认为两行匹配。
# left1 右表：4 行，键值组合为 (K0,K0)、(K0,K1)、(K1,K0)、(K2,K1)；
# right1 右表：4 行，键值组合为 (K0,K0)、(K1,K0)、(K1,K0)、(K2,K0)。
left1 = pd.DataFrame({'key1':['K0','K0','K1','K2'],'key2':['K0','K1','K0','K1'],'A':['A1','A2','A3','A4'],'B':['B1','B2','B3','B4']},index=[0,1,2,3])
right1 = pd.DataFrame({'key1':['K0','K1','K1','K2'],'key2':['K0','K0','K0','K0'],'C':['C1','C2','C3','C4'],'D':['D1','D2','D3','D4']},index=[0,1,2,3])

# print(left1) / print(right1)：查看多键表。
print(left1)
print(right1)

# how='inner'：内连接，只保留两边 key1、key2 都匹配上的组合。
#   匹配结果：(K0,K0) 匹配 1 次；(K1,K0) 匹配 2 次（右表有两行 K1,K0），
#   所以最终 3 行。
# indicator=True：自动新增一列 _merge，标注每行的来源：
#   both        —— 该行是两边匹配成功的结果；
#   left_only   —— 只出现在左表；
#   right_only  —— 只出现在右表。
# 用 indicator 可以一眼看出哪些数据是"两边都有"、哪些是"单边独有"。
res5 = pd.merge(left1,right1,on=['key1','key2'],how='inner',indicator=True)
print(res5)

# how='outer'：外连接（并集），两边的行全部保留：
#   both 的 3 行之外，还包含：
#   left_only 2 行：左表独有的 (K0,K1)、(K2,K1)；
#   right_only 1 行：右表独有的 (K2,K0)。
# 对不上的那一侧，列值自动填 NaN。
# 最终 6 行。
res6 = pd.merge(left1,right1,on=['key1','key2'],how='outer',indicator=True)
print(res6)

# how='left'：左连接，以左表为基准，左表的行全部保留；
# 右表只提供能匹配上的列，匹配不到的位置填 NaN。
# indicator='indicator_column'：把来源列重命名为 indicator_column，
# 而不是默认的 _merge。
# 本例左表 4 行全部保留，其中 (K1,K0) 能匹配到右表两行，所以结果是 5 行。
res7 = pd.merge(left1,right1,on=['key1','key2'],how='left',indicator='indicator_column')
print(res7)

# how='right'：右连接，以右表为基准，右表的行全部保留；
# 左表匹配不到的位置填 NaN。
# 本例右表 4 行全部保留（右表每个 (K1,K0) 都只能匹配左表 1 行），结果 4 行。
res8 = pd.merge(left1,right1,on=['key1','key2'],how='right',indicator='indicator_column')
print(res8)

# 用"行索引"做连接键：
#   left_index=True, right_index=True 表示不按列连接，
#   而是用左右两边的行索引进行匹配。
# 本例 left1、right1 的行索引都是 0、1、2、3，完全一致，
# 所以 how='inner' 的结果是 4 行；列取两边的并集：
#   key1、key2 两边都有（保留一份）、A、B 来自左表、C、D 来自右表。
res9 = pd.merge(left1,right1,left_index=True,right_index=True,how='inner')
print(res9)

# 同样按行索引连接，但 how='outer'：由于两边索引完全相同，
# 结果和 inner 一样都是 4 行；若索引有差异，外连接会补 NaN。
res10 = pd.merge(left1,right1,left_index=True,right_index=True,how='outer')
print(res10)

# 处理"重名列"：boys、girls 两张表都有 age 列，
# 直接 merge 后两列重名，pandas 默认会加 _x、_y 后缀区分，
# 但更直观的做法是自己用 suffixes 指定后缀。
boys = pd.DataFrame({'k':['K0','K1','K2'],'age':[10,15,20]})
girls = pd.DataFrame({'k':['K0','K0','K3'],'age':[20,25,30]})

# print(boys) / print(girls)：查看两张带重名列的表。
print(boys)
print(girls)

# pd.merge(boys, girls, on='k', how='outer', suffixes=('_boy','_girl'))：
#   on='k'：按 k 列连接；
#   how='outer'：k 取两边的并集 K0、K1、K2、K3；
#   suffixes=('_boy','_girl')：左表 age 列改名 age_boy，
#       右表 age 列改名 age_girl，避免重名冲突。
# 结果说明：
#   K0：左表 1 行 × 右表 2 行 = 2 行（多对多会产生笛卡尔积式的组合）；
#   K1、K2：只有左表，右表 age_girl 为 NaN；
#   K3：只有右表，左表 age_boy 为 NaN；
#   总共 5 行。
res11 = pd.merge(boys,girls,on='k',how='outer',suffixes=('_boy','_girl'))
print(res11)


# ------------------------------------------------------------
# 13. 绘图：pandas 自带的 plot 与 matplotlib 联用
# ------------------------------------------------------------
# pandas 的 plot 底层就是 matplotlib，所以可以直接 plt.show() 显示图形。
# 注意：本段绘图与前面的数据分析无直接关系，只是演示可视化方法。

# np.random.randn(1000)：生成 1000 个标准正态分布随机数；
# index=np.arange(1000)：行索引为 0~999；
# 再用 pd.Series(...) 包成一维序列。
data1 = pd.Series(np.random.randn(1000),index=np.arange(1000))

# cumsum()：对序列做累加求和（第 i 项 = 前 i 项之和）。
# 原本杂乱无章的随机数累加后，会变成一条有明显走势的"随机游走"曲线，
# 更便于观察趋势变化。
data1 = data1.cumsum()

# plot()：绘制折线图。Series 默认以行索引为 x 轴、值为 y 轴。
# plot 默认 kind='line'（折线图），还可通过 kind 换成其他图形：
#   kind='bar'  柱状图     kind='barh' 横向柱状图
#   kind='hist' 直方图     kind='box'  箱线图
#   kind='pie'  饼图       kind='area' 面积图
data1.plot()

# plt.show()：把画布显示出来（在脚本中必须调用，否则不显示）。
# 在 Jupyter Notebook 中可改为 %matplotlib inline，无需调用 show；
# 在普通脚本里 show() 会阻塞程序，直到手动关闭弹出的图形窗口。
plt.show()

# 生成 1000 行 4 列的随机数矩阵：
#   columns=list('ABCD')：列名 A、B、C、D；
#   index=np.arange(1000)：行索引 0~999。
data2 = pd.DataFrame(np.random.randn(1000,4),index=np.arange(1000),columns=list('ABCD'))

# head()：默认显示前 5 行，用来快速预览数据是否正常。
print(data2.head())

# 同样做累加，让各列呈现趋势。
data2 = data2.cumsum()

# plot()：DataFrame 的折线图，默认每列画一条线，并自动加图例。
data2.plot()

# plot.scatter(...)：绘制散点图。
#   x='A', y='B'：以 A 列为横坐标、B 列为纵坐标；
#   color='red'：散点颜色；
#   label='Class 1'：图例标签。
# 返回坐标轴对象 ax，便于后续把第二张图叠加到同一张画布上。
# 其他常用参数：marker='o'（点的形状）、s=10（点的大小）、alpha=0.8（透明度）。
ax = data2.plot.scatter(x='A',y='B',color='red',label='Class 1')

# 第二次 plot.scatter 传入 ax=ax：
#   表示把蓝色散点画在刚才的同一个坐标系里，
#   从而在一张图上同时展示 A-B 和 A-C 两组关系。
data2.plot.scatter(x='A',y='C',color='blue',label='Class 2',ax=ax)

# 显示叠加后的散点图。
plt.show()
