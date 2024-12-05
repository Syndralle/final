import matplotlib.pyplot as plt
import numpy as np

# 模拟数据
x = np.linspace(0, 10, 500)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(2 * x)

# 创建主图
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x, y1, label="sin(x)")
ax.plot(x, y2, label="cos(x)")
ax.plot(x, y3, label="sin(2x)")
ax.set_xlabel("X-axis", fontsize=14, family='serif')
ax.set_ylabel("Y-axis", fontsize=14, family='serif')
ax.set_title("Dense Curves with Zoom-In Region", fontsize=18, family='serif')
ax.legend()

# 添加局部放大视图
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset

# 创建放大区域
axins = inset_axes(ax, width="40%", height="40%", loc='upper right')  # 放大区域位置
axins.plot(x, y1, label="sin(x)")
axins.plot(x, y2, label="cos(x)")
axins.plot(x, y3, label="sin(2x)")

# 设置放大区域的坐标范围
x1, x2 = 4, 6   # X轴放大范围
y1, y2 = 0, 0.5  # Y轴放大范围
axins.set_xlim(x1, x2)
axins.set_ylim(y1, y2)

# 去掉放大区域的多余刻度
axins.set_xticks([])
axins.set_yticks([])

# 添加指示框和连接线
mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="0.5")

# 显示图形
plt.tight_layout()
plt.show()
