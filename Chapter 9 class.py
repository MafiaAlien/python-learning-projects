# class Dog():
# 	# 模拟小狗的各种动作
# 	def __init__(self, name, age):
# 		# 初始化属性name和age
# 		self.name = name
# 		self.age = age
#
# 	def sit(self):
# 		# 模拟小狗被命令蹲下
# 		print(self.name.title() + ' is now sitting.')
#
# 	def roll_over(self):
# 		# 模拟小狗被命令时打滚
# 		print(self.name.title() + ' rolled over!')
#
#
# my_dog = Dog('Max', '6')
# my_dog.sit()
# my_dog.roll_over()

# 9-1 9-2
# class Restaurant():
# 	def __init__(self, restaurant_name, cuisine_type):
# 		self.name = restaurant_name
# 		self.cuisine = cuisine_type
#
# 	def describe_restaurant(self):
# 		print('Our restaurant ' + self.name.title() + " 's business hour is from 10:00 AM to 10:00 PM")
#
# 	def open_restaurant(self):
# 		print('\tour main dish is ' + self.cuisine.title())
#
#
# haidilao = Restaurant('海底捞', '火锅')
#
# haidilao.describe_restaurant()
# haidilao.open_restaurant()
#
# mzdp = Restaurant('眉州东坡','川菜')
# mzdp.describe_restaurant()
# mzdp.open_restaurant()
#
# xiangcunji = Restaurant('乡村基','快餐')
# xiangcunji.describe_restaurant()
# xiangcunji.open_restaurant()

# class User():
# 	def __init__(self, first_name, last_name):
# 		self.first = first_name
# 		self.last = last_name
#
# 	def describe_user(self):
# 		print('Your first name is %s ' % (self.first))
# 		print('and your last name is %s ' % (self.last))
#
# 	def greet_user(self):
# 		print('Greeting!,' + self.first.title() + self.last.title())
#
# WY = User ('Yue','Wang')
# WY.describe_user()
# WY.greet_user()

# 汽车的类
# class Car():
# 	def __init__(self, make, model, year):
# 		self.make = make
# 		self.model = model
# 		self.year = year
# 		self.odo = 0
#
# 	def get_descriptive_name(self):
# 		"返回整洁的描述性信息"
# 		long_name = str(self.year) + ' ' + self.make + " " + self.model
# 		return long_name.title()
#
# 	def read_odo(self):
# 		return 'This vehicle has %s' % (self.odo) + ' miles on it'
#
#
# new_car = Car('Toyota', 'Camery', '2019')
# print(new_car.get_descriptive_name())
# print(new_car.read_odo())


# 9-4
# class Restaurant():
# 	def __init__(self, restaurant_name, cuisine_type):
# 		self.name = restaurant_name
# 		self.cuisine = cuisine_type
# 		self.number_served = 0
#
# 	def describe_restaurant(self):
# 		print('Our restaurant ' + self.name.title() + " 's business hour is from 10:00 AM to 10:00 PM")
#
# 	def open_restaurant(self):
# 		print('\tour main dish is ' + self.cuisine.title())
#
# 	def set_number_served(self, new_number):
# 		self.number_served = new_number
#
# 	def increment_number_served(self, add_number_served):
# 		self.number_served += add_number_served


# haidilao = Restaurant('海底捞', '火锅')
#
# haidilao.describe_restaurant()
# haidilao.open_restaurant()
#
# mzdp = Restaurant('眉州东坡','川菜')
# mzdp.describe_restaurant()
# mzdp.open_restaurant()

# xiangcunji = Restaurant('乡村基', '快餐')
# xiangcunji.describe_restaurant()
# xiangcunji.open_restaurant()
# xiangcunji.set_number_served(15)
# print(xiangcunji.number_served)
# add_number = xiangcunji.increment_number_served(60)
# print(xiangcunji.number_served)


# 9-5
# class User():
# 	def __init__(self, first_name, last_name):
# 		self.first = first_name
# 		self.last = last_name
# 		self.login_attempts = 0
#
# 	def describe_user(self):
# 		print('Your first name is %s ' % (self.first))
# 		print('and your last name is %s ' % (self.last))
#
# 	def greet_user(self):
# 		print('Greeting!,' + self.first.title() + self.last.title())
#
# 	def increment_login_attempts(self):
# 		self.login_attempts += 1
# 		print('Login time add 1 more')
# 		print('Login time is %s'%(self.login_attempts))
# 		print('===分割线===')
#
# 	def reset_login_attempts(self):
# 		self.login_attempts = 0
# 		print('Login time is reseted back to 0')
#
# WY = User ('Yue','Wang')
# WY.describe_user()
# WY.greet_user()
# WY.increment_login_attempts()
# WY.increment_login_attempts()
# WY.increment_login_attempts()
# print(WY.login_attempts)
# WY.reset_login_attempts()
# print(WY.login_attempts)

# 汽车的类
# class Car():
# 	def __init__(self, make, model, year):
# 		self.make = make
# 		self.model = model
# 		self.year = year
# 		self.odo = 0
#
# 	def get_descriptive_name(self):
# 		"返回整洁的描述性信息"
# 		long_name = str(self.year) + ' ' + self.make + " " + self.model
# 		return long_name.title()
#
# 	def read_odo(self):
# 		return 'This vehicle has %s' % (self.odo) + ' miles on it'
#
# 	def update_odo(self, miles):
# 		if miles >= self.odo:
# 			self.odo = miles
# 		else:
# 			print('You cannot roll back odo!')
#
# 	def increment_odo(self, miles):
# 		self.odo += miles
#
#
# class electri_cars(Car):
# 	def __init__(self, make, model, year):
# 		"""初始化父类属性"""
# 		super().__init__(make, model, year)

# Icecream
# class Restaurant():
# 	def __init__(self, restaurant_name, cuisine_type):
# 		self.name = restaurant_name
# 		self.cuisine = cuisine_type
# 		self.number_served = 0
#
# 	def describe_restaurant(self):
# 		print('Our restaurant ' + self.name.title() + " 's business hour is from 10:00 AM to 10:00 PM")
#
# 	def open_restaurant(self):
# 		print('\tour main dish is ' + self.cuisine.title())
#
# 	def set_number_served(self, new_number):
# 		self.number_served = new_number
#
# 	def increment_number_served(self, add_number_served):
# 		self.number_served += add_number_served
#
#
# class IceCreamStand(Restaurant):
# 	def __init__(self, restaurant_name, cuisine_type):
# 		super().__init__(restaurant_name, cuisine_type)
#
# 	def flavors(self, *flavor):
# 		flavor_lst = list()
# 		flavor_lst.append(flavor)
# 		print('\tOur flavors have ',flavor_lst)
#
#
# DQ = IceCreamStand(' Dairr Queen', 'Icecream')
# DQ.describe_restaurant()
# DQ.open_restaurant()
# DQ.flavors('Starw berry', 'Pineapple', 'Watermelon', 'Apple')


# class User():
# 	def __init__(self, first_name, last_name):
# 		self.first = first_name
# 		self.last = last_name
# 		self.login_attempts = 0
#
# 	def describe_user(self):
# 		print('Your first name is %s ' % (self.first))
# 		print('and your last name is %s ' % (self.last))
#
# 	def greet_user(self):
# 		print('Greeting!,' + self.first.title() + self.last.title())
#
# 	def increment_login_attempts(self):
# 		self.login_attempts += 1
# 		print('Login time add 1 more')
# 		print('Login time is %s' % (self.login_attempts))
# 		print('===分割线===')
#
# 	def reset_login_attempts(self):
# 		self.login_attempts = 0
# 		print('Login time is reseted back to 0')
#
#
# class Privileges():
# 	def show_privileges(self):
# 		privileges = ['can add post', 'can delete post', 'can ban user']
# 		print('you have following privileges: ')
# 		print(privileges)
#
#
# class Admin(User):
# 	def __init__(self, first_name, last_name):
# 		super().__init__(first_name, last_name)
# 		self.privileges = Privileges()
#
#
# WY = Admin('Yue', 'Wang')
# WY.describe_user()
# WY.privileges.show_privileges()

from random import randint

#多面骰子
# class Die():
# 	def __init__(self, sides):
# 		self.sides = sides
#
# 	def roll_die(self, times):
# 		while True:
# 			number = randint(1, self.sides)
# 			if times > 0:
# 				print(number)
# 				times -= 1
# 				continue
# 			else:
# 				print('Times out, Game Over!')
# 				print('***分隔符***')
# 				break
#
#
# new_die = Die(6)
# new_die.roll_die(10)
#
# new_die = Die(10)
# new_die.roll_die(10)
#
# new_die = Die(20)
# new_die.roll_die(10)
