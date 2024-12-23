import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# 设置学术风格
sns.set_theme(style="whitegrid")

categories = ['ALL', 'OC', 'FM', 'IC', 'DBC', 'TS']
val1 = [1500, 356, 0, 133, 887, 581]
val2 = [1500, 0, 183, 8, 1310, 950]

# 创建柱状图
fig, ax = plt.subplots(figsize=(8, 5))  # 设置图表大小

x = np.arange(len(categories))
width = 0.2
bars1 = ax.bar(x - width / 2, val1, width, label='dataset1', color='skyblue', edgecolor='black')
bars2 = ax.bar(x + width / 2, val2, width, label='dataset2', color='lightcoral', edgecolor='black')

# 添加数值标签
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        # ax.text(bar.get_x() + bar.get_width() / 2, height + 1, f'{height}', 
        #         ha='center', va='bottom', fontsize=10)

# 图表标题和轴标签
ax.set_title('Quantity Attributes', fontsize=14, weight='bold', fontfamily='serif')
# ax.set_xlabel('', fontsize=12)
# ax.set_ylabel('Values', fontsize=12)

# 设置分类标签
ax.set_xticks(x)
ax.set_xticklabels(categories)

# 添加图例
ax.legend(fontsize=10)

ax.grid(axis = 'x')
# 去除顶部和右侧边框
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 优化布局
plt.tight_layout()

# 保存图表为高分辨率图片（可选）
plt.savefig('grouped_bar_chart.png', dpi=300)

# 显示图表
plt.show()
