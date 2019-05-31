#Exercise page 54
# for i in range(21):
#     print(i)

# lic = range(1,1000001)
# print(max(lic))
# print(min(lic))
# print(sum(lic))

#打印10到20中的奇数
# for i in range(10,20,1):
#     if i%2 != 0:
#         print (i)

#打印3到30中3的倍数
# lic = range(3,31)
# for i in lic:
#     if i%3 ==0:
#         print(i)

#打印1到10当中所有整数的立方
# lic = range(1,11)
# for i in lic:
#     print(i**3)

#使用列表解析式生成列表包含前十个数的立方

# lic = [i**3 for i in range(1,11)]
# print(lic)

#切片
# players = ['a','b','c','d']
# print(players[-3:])

# sentence = 'The first three items in the list are ：'
# for words in sentence :
# 	words = sentence.split()
# 	print(words)

#如果外星人是绿色，玩家得5分，如果外星人不是绿色，玩家得10分
# alien_colors = ['green','yellow','red']
# for color in alien_colors:
# 	if color == 'green':
# 		print('The player killed a green alien, getting 5 credits')
# 	else:
# 		print('The player get 10 credits')

# alien_colors = ['green','yellow','red']
# for color in alien_colors:
# 	if color =='green':
# 		print('player get 5 points')
# 	elif color =='red':
# 		print('player get 10 points')
# 	elif color == 'yellow':
# 		print("player get 10 points")

#Exercise on Page 79
#5-8
# users = ['WY','LZH','admin','NK','Eric']
# for user in users:
# 	if user == 'admin':
# 		print('Hello admin, would you like to see a status report?')
# 	else:
# 		print('Hello %s, would you like to see a status report?' %(user))

#5-9
# users = []
# if len(users)> 0  :
# 	print('Good ,there is at least one user ')
# elif len(users) == 0:
# 	print('We need to find some users!')


#5-10 检查两个列表中相同元素，不区分大小写。
# current_users = ['WY','LZH','admin','NK','Eric']
# new_users = ['wy','lzh','AAA','BBB','CCC']
#
# for user in new_users:
# 	if user.lower() in [current_users.lower() for current_users in current_users]:
# 		print('Sorry, %s  has been registered, please use another user name'%(user))
# 	else:
# 		print('Congratulation! %s has not been registred'%(user))

