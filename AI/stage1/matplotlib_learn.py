"""
matplotlib 绘图入门练习

本文件演示了 matplotlib 最基本的使用流程：
1. 用 numpy 生成一组 x 坐标数据；
2. 根据 x 计算出两条曲线的 y 值；
3. 创建两个独立的图形窗口（figure），分别绘制两条曲线；
4. 用 plt.show() 一次性弹出所有窗口进行展示。
"""

# 导入 matplotlib 的绘图模块 pyplot，并给它起别名 plt。
# pyplot 提供了一套类似 MATLAB 的绘图接口，是 matplotlib 中最常用的模块。
import matplotlib.pyplot as plt

# 导入 numpy 数值计算库，并给它起别名 np。
# 这里用它生成坐标数据，并对数组进行数学运算。
import numpy as np

# 生成 x 轴的坐标点：
# np.linspace(开始值, 结束值, 点的个数) 会在 [-3, 3] 这个闭区间内
# 均匀地取 50 个点（包含首尾两个端点），返回一个一维 numpy 数组。
x = np.linspace(-3, 3, 50)

# 第一条曲线：y1 = 2x + 1，是一条斜率为 2、截距为 1 的直线。
# 因为 x 是 numpy 数组，这里会自动进行"向量化"运算，
# 即对数组中的每个元素都计算一次 2*x+1，结果仍是长度相同的数组。
y1 = 2 * x + 1

# 第二条曲线：y2 = x^2，是一条开口向上的抛物线。
# x ** 2 同样是对数组逐元素求平方，而不是数学上的矩阵乘方。
y2 = x ** 2

# 创建第 1 个图形窗口（figure）：
# num=1  给窗口编号为 1，之后再次使用该编号时可以复用这个窗口；
# figsize=(8,5)  设置窗口尺寸为宽 8 英寸、高 5 英寸（1 英寸约 2.54 厘米）。
# 执行完这行后，后面所有绘图操作都会默认画在这个窗口里。
plt.figure(num=1, figsize=(8,5))

# 在窗口 1 中绘制第一条曲线：
# x, y1        分别是横坐标和纵坐标的数据；
# color='gray' 线条颜色设为灰色；
# linewidth=1.0  线条粗细为 1.0（单位是磅）；
# linestyle='--' 线型设为虚线（--），其他常用线型有 '-'实线、':'点线、'-.'点划线。
plt.plot(x, y1,color='gray',linewidth=1.0,linestyle='--')


# 创建第 2 个图形窗口，编号为 2，尺寸为 10 英寸 × 10 英寸。
# 注意：这与窗口 1 相互独立，前面的直线不会被画到这张图上。
plt.figure(num=2, figsize=(10,10))

# 在窗口 2 中绘制第二条曲线：
# color='red'  线条颜色设为红色；
# linewidth=1.0  线条粗细为 1.0；
# linestyle='-'  线型设为实线。
plt.plot(x, y2,color='red',linewidth=1.0,linestyle='-')

# 设置 x 轴的显示范围为 -1 到 2。
# 注意：这里只改变坐标轴的"视图窗口"（即显示多少范围的数据），
# 不会修改数据本身；超出这个范围的数据点会被裁剪掉，不再显示。
plt.xlim(-1,2)

# 设置 y 轴的显示范围为 -2 到 3。
# 与 xlim 同理，用于控制纵轴可见的数值区间。
plt.ylim(-2,3)

# 设置 x 轴的标签文字为 'x'。
# 标签默认显示在 x 轴下方、靠近中间的位置。
plt.xlabel('x')

# 设置 y 轴的标签文字为 'y'。
# 标签默认显示在 y 轴左侧、靠近中间的位置。
plt.ylabel('y')

# 生成 x 轴刻度的位置：
# np.linspace(-1, 2, 5) 会在闭区间 [-1, 2] 内均匀地取 5 个点，
# 得到的结果约为 [-1.0, -0.25, 0.5, 1.25, 2.0]。
# 这里先把这些刻度位置保存到变量 new_ticks 中，稍后用于设置 x 轴刻度。
new_ticks = np.linspace(-1,2,5)

# 设置 x 轴的刻度位置：
# 只传入一个参数时，表示刻度要显示在这些数值位置上，
# 刻度标签会自动使用对应的数值（采用 matplotlib 的默认数字格式）。
plt.xticks(new_ticks)

# 设置 y 轴的刻度位置以及每个刻度对应的标签：
# 第一个列表 [-2, -1.8, -1, 1.22, 3] 是刻度的实际位置（数据坐标）；
# 第二个列表是与之一一对应的标签文字，两个列表长度必须相同。
# 标签使用了 LaTeX 数学公式语法：用一对 $ 把内容包起来，即可渲染公式效果。
# 字符串前面的 r 表示"原始字符串"，让反斜杠 \ 保持原样，不被 Python 转义。
# 各标签含义如下：
#   r'$really\ bad$'   ->  "really bad"（\ 后面接空格表示一个普通空格）
#   r'$bad\ \alpha$'   ->  "bad α"（\alpha 是希腊字母 α）
#   r'$normal$'        ->  普通文字 "normal"
#   r'$good$'          ->  普通文字 "good"
#   r'$really\ good$'  ->  "really good"
plt.yticks([-2,-1.8,-1,1.22,3],
           [r'$really\ bad$',r'$bad\ \alpha$',r'$normal$',r'$good$',r'$really\ good$'])

# 获取当前图形窗口（这里是窗口 2）的坐标轴对象（Axes）。
# gca 是 "get current axes"（获取当前坐标轴）的缩写。
# 前面使用的 plt.xlim、plt.plot 等是"面向过程"的快捷写法，
# 它们内部实际也是在操作这个 Axes 对象；
# 拿到 ax 之后，就可以用"面向对象"的方式对坐标轴做更精细的控制。
ax = plt.gca()

# 一个坐标轴四周有四条"脊线"（spines）：top、bottom、left、right。
# 它们构成坐标轴最外层的边框。下面通过修改脊线，把默认的
# "盒子形"边框改成常见的"十字形"坐标轴，使 x、y 轴交于原点 (0, 0)。

# 把右侧脊线（右边框）的颜色设为 'none'，即完全隐藏右边的边框线。
ax.spines['right'].set_color('none')

# 把顶部脊线（上边框）的颜色设为 'none'，即完全隐藏上边的边框线。
ax.spines['top'].set_color('none')

# 设置 x 轴刻度只显示在 bottom（下方）这条脊线上。
# 默认情况下 top 和 bottom 两条边都会显示刻度，这里只保留下方。
ax.xaxis.set_ticks_position('bottom')

# 设置 y 轴刻度只显示在 left（左侧）这条脊线上。
# 默认情况下 left 和 right 两条边都会显示刻度，这里只保留左侧。
ax.yaxis.set_ticks_position('left')

# 把 bottom（下方）脊线移动到 y=0 的位置（使用数据坐标）。
# 参数 ('data', 0) 中：'data' 表示采用数据坐标系，0 表示目标位置。
# 效果是让 x 轴经过 y=0，形成穿过原点的水平坐标轴。
ax.spines['bottom'].set_position(('data',0))

# 把 left（左侧）脊线移动到 x=0 的位置（使用数据坐标）。
# 效果是让 y 轴经过 x=0，形成穿过原点的竖直坐标轴。
# 经过上面两步后，x 轴与 y 轴便在原点 (0, 0) 处相交。
ax.spines['left'].set_position(('data',0))

# 显示所有已经创建的图形窗口。
# 程序运行到这里会阻塞，弹出窗口供你查看；
# 关掉所有窗口后，程序才会继续往下执行并结束。
plt.show()
