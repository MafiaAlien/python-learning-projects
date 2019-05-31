import matplotlib.pyplot as plt

x_values = range(1,5001)
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, s = 40 )

plt.title('Cubic Numbers', fontsize = 24)
plt.xlabel('Values', fontsize = 14)
plt.ylabel('Cubic values', fontsize = 14)

plt.tick_params(axis = 'both', which = 'major', fontsize = 14)
plt.axis([0, 5100, 0, 51000000000000])

plt.show()


