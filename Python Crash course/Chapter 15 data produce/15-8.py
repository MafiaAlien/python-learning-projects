from die import Die
import pygal

die_1 = Die()
die_2 = Die()
die_3 = Die()


# 骰子结果展示
results = []
for roll_num in range(1000):
	result = die_1.roll() + die_2.roll() + die_3.roll()
	results.append(result)

# 骰子结果出现频率
frequencies = []
max_result = die_1.sides + die_2.sides + die_3.sides
for value in range(3, max_result + 1):
	frequency = results.count(value)
	frequencies.append(frequency)

print(results)
print(frequencies)

# 结果可视化
hist = pygal.Bar()

hist.title = 'Results of rolling two D8 1000 times.'
hist.x_labels = ['3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18']
hist.x_title = 'Result'
hist.y_title = 'Frenquency of Result'

hist.add('D6 + D6 + D6', frequencies)
hist.render_to_file('15-8_three_dice_6_sides_visual.svg')