import matplotlib.pyplot as plt
from random_walk import RandomWalk



while True:
	rw = RandomWalk()
	rw.fill_walk()
	plt.scatter(rw.x_values, rw.y_values, s=15)
	plt.show()

	point_numbers = list(range(rw.num_points))
	plt.scatter(rw.x_values, rw.y_values, c=point_numbers,
				cmap=plt.cm.Blues, edgecolor='none', s=15)
	keep_running = input('Make another walk? (Y/N)')
	if keep_running == 'N' or keep_running == 'n':
		break
