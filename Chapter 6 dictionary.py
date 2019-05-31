# Exercise on Page 87
# 6-1
# name_add = {'WY':'CD','LZH':'LA','NK':'NB','WYD':'XA'}
# print(name_add)

# 6-2
# 6-5:  you need to create a dictionary and store three main rivers and the countries which the rivers pass. for exmaple: 'Nile':'Egypy'
# rivers_countries = {'Nile':'Egypt','Amazon':'Peru','Huanghe':'China','Mississippi':'US'}
# for r,c in rivers_countries.items():
# 	print('The %s runs through %s' %(r,c))
# print(rivers_countries.keys())
# print(rivers_countries.values())

# 6-8  you need to create multiple dictionaries, naming them by pets' name; the dictionaries contain species and hosts' names; Finally , you save these dictionaries in a list which name is 'pets', then iterate the list and print out the keys and values.
# Bread = {'Puppy':['dog','Jim']}
# Cookie = {''}

# 6-9 loved places:
favorite_places = {'Jim': 'LA',
				   'Jack': 'SF',
				   'Trump': 'Shanghai',
				   'LZH': ['LA', 'Chengdu'],
				   'WY': ['DC', 'Chongqing']}
for name, place in favorite_places.items():
	print('Name:', name)
	print('\tFavorite place:', place)
