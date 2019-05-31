# 8-1
# def display_message():
# 	print('What I learn in this chapter is function')
#
# display_message()

# 8-2
# def favorite_book(title):
# # 	print('One of my favorite book is',title)
# #
# # favorite_book('Principle')

# def describe_pet(pet_name,animal_type = 'dog'):
# 	print('\nI have a '+ animal_type + '.')
# 	print('\nMy ' + animal_type + "'s name is " + pet_name.title()+ '.')
#
# describe_pet('Willie')

# 8-3
# you need to program a function named 'make_skirt()',and let it accept a size and logo that brand on t-shirt;
# then using this function, you need to print a sentence which express the size and logo of the t-shirt
# def make_shirt(size, logo):
# 	print("This t-shirt's size is "+ size.title() + " and logo is "+ logo.title())
#
# make_shirt('5','Skull')
# make_shirt(logo = 'Frog',size = '6')

# 8-5: you need to program a function whose name is 'describe_city()' and which receive names and countries of certain city.
# Then, this function can print a simple sentence such as 'Reykjavik is in Iceland'. Moreover ,you need to set up a default
# value to save countries ,use this function for 3 different cities and make sure that at least one city is not in default  country.
# def describe_city(name,country = 'United States'):
# 	print(name.title() + ' is in '+ country)
#
# describe_city('Chicago')
# describe_city('Los Angeles')
# describe_city('San Jose')
# describe_city('Chengdu',country = 'China')
# describe_city('Tokyo', country = 'Japan')

# 8-6: you need to program a function named 'city_country()' and accepting names and countries of certain cities. Then
# return strings whose format is 'Santiago, Chile'.Finally, you need to use at least three cities and countries in this
# function and return the value.
# def city_country(city_name, country):
# 	information = {'City name: ':city_name,'City country: ':country}
# 	return information
# print(city_country('Tokyo','Japan'))

# 8-7: you need to write a program named 'make_album()', which can create a dictionary that describes the musical album;
# this function can save the names of singers and albums, and print the return value. you need to use this function to
# create three different dictionaries which represent varied albums, and to print the return value.
# def make_album(singer, album_name,songs = ''):
# 	information = {"Singer's name : ":singer, "Album's name: ":album_name}
# 	if songs:
# 		information['songs'] = songs
# 	return information
# print(make_album('周杰伦','七里香'))
# print(make_album('王力宏','盖世英雄'))
# print(make_album('Jackson','blue jeans','10000'))

# 8-8: you need to program a whle iteration and allow user to type in a singer and name of album.

# def make_album(singer, album_name,songs = ''):
# 	information = {"Singer's name : ":singer, "Album's name: ":album_name}
# 	if songs:
# 		information['songs'] = songs
# 	return information
# print(make_album('周杰伦','七里香'))
# print(make_album('王力宏','盖世英雄'))
# print(make_album('Jackson','blue jeans','10000'))


# from collections import OrderedDict
# def make_album():
# 	information = list()
# 	while True :
# 		singer = input("Enter a singer's name : ")
#
# 		if singer == 'quit':
# 			print('you have already quited ')
# 			break
#
# 		album_name = input("Enter a album's name : ")
#
# 		if album_name == 'quit':
# 			print('you have already quited ')
# 			break
#
# 		info_dict = OrderedDict(Singer_name=singer, Album_name=album_name)
# 		information.append(info_dict)
# 	print(information)


# 8-9
# magician_names = ['a','b','c','d','e']
# copy_magiacian_names = sorted(magician_names[:],reverse = True)
# the_great = []
# def show_magicians(names):
# 	for name in names:
# 		the_great.append(name)
#
#
# def make_great(magicians):
# 	for magician in magicians:
# 		print('the great %s'%(magician))
#
# print('List number 1: ')
# show_magicians(copy_magiacian_names)
# make_great(the_great)
#
#
# print('\nList number 2: ')
# show_magicians(magician_names)
# make_great(the_great)

# 8-12 ：you need to define a function, which receives any ingredients that customers want to add.
# def ingredients(*toppings):
# 	print('Customers need following pizza topping: ' )
# 	for ingredient in toppings:
# 		print('-'+ ingredient)
#
# ingredients('mushrooms','hams','turkey','spam','pineapples')

# 8-13
# def build_profile(first, last, **user_info):
# 	#创建一个字典，其中包含我们知道的有关用户的一切
# 	profile = {}
# 	profile['first name'] = first
# 	profile['last name'] = last
# 	for key, value in user_info.items():
# 		profile[key] = value
# 	return profile
#
# user_profile = build_profile('albert','esinstein',location = 'princeton',field = 'physics')
# print(user_profile)
#
# user_profile = build_profile('子豪','李',food = '火锅', hobby = '看书')
# print(user_profile)

# 8-12: you  create a function which can receive any information of a vehicle.
# def buid_vehicle_info(manufacturer,make, **other_info):
# 	car_info = {}
# 	car_info['Manufacturer ; '] = manufacturer
# 	car_info["Car's make : "] = make
# 	for k, v in other_info.items():
# 		car_info[k] = v
# 	return car_info
#
# print(buid_vehicle_info('TOYOTA','Camery',year = '2012', model = 'Sedan', color = 'Blue',tow_package  = True))

# 装饰器


