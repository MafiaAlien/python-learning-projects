# 汽车的类
class Car():
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odo = 0

	def get_descriptive_name(self):
		"返回整洁的描述性信息"
		long_name = str(self.year) + ' ' + self.make + " " + self.model
		return long_name.title()

	def read_odo(self):
		return 'This vehicle has %s' % (self.odo) + ' miles on it'

	def update_odo(self, miles):
		if miles >= self.odo:
			self.odo = miles
		else:
			print('You cannot roll back odo!')

	def increment_odo(self, miles):
		self.odo += miles


class ElectricCars(Car):
	def __init__(self, make, model, year):
		"""初始化父类属性"""
		super().__init__(make, model, year)