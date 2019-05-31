import json

# filename = 'username.json'
# try:
# 	with open(filename) as f_obj:
# 		username = json.load(f_obj)
# except FileNotFoundError:
# 	username = input('What is your name? ')
# 	with open(filename,'w') as f_obj:
# 		json.dump(username,f_obj)
# 		print('We will remember you when you come back. %s!'%(username))
# else:
# 	print('Welcome back, %s'%(username) + '!')

#10-11 10-12
filename = 'favorite_number.json'

# def input_num():
# 	with open(filename,'w')as f_obj:
# 		new_num = input('Please enter your favorite number: ')
# 		json.dump(new_num,f_obj)

def load_num():
	try:
		with open(filename) as f_obj:
			number = json.load(f_obj)
	except:
		with open(filename,'w') as f_obj:
			number = input('I cannot find a number, please enter your favorite number: ')
			json.dump(number,f_obj)
			print('We will remember your number when you come back.')
	else:
		print("I know your favorite number ! it's: %s" % (number))


load_num()