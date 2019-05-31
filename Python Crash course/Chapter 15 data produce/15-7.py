from die import Die
import pygal

die_1 = Die(8)
die_2 = Die(8)


# 骰子结果展示
results = []
for roll_num in range(1000):
	result = die_1.roll() + die_2.roll()
	results.append(result)

# 骰子结果出现频率
frequencies = []
max_result = die_1.sides + die_2.sides
for value in range(2, max_result + 1):
	frequency = results.count(value)
	frequencies.append(frequency)

print(results)
print(frequencies)

# 结果可视化
hist = pygal.Bar()

hist.title = 'Results of rolling two D8 1000 times.'
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = 'Result'
hist.y_title = 'Frenquency of Result'

hist.add('D8 + D8', frequencies)
hist.render_to_file('dice_8_sides_visual.svg')