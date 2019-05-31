import matplotlib.pyplot as plt

x_value = list(range(1, 1001))
y_value = [x ** 2 for x in x_value]

plt.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Blues, edgecolors='none', s=40)
# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置坐标轴取值范围
plt.axis([0, 1100, 0, 1100000])

# 设置刻度标记大小
plt.tick_params(axis='both', which='major', labelsize=14)

plt.savefig('squares_plot.png', bbox_inches = 'tight')
