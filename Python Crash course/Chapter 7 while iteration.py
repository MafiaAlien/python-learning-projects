# #7-1
# car = input('What brand of car do you need right now:')
# print ('Let me see if I can find you a', car)
#
# 7-2
#  num_people = int(input('How many people will come to dinner: '))
#  if num_people > 8:
#  	print('Sorry , we do not have available tables for people whose number beyond 8')
# else:
# 	print('Congratulations, your reservation has been made.')
#
# num = int(input('Please enter a number: '))
# if num % 10 == 0:
# 	print("The number you type in is a multiple of 10.")
# else:
# 	print('The number you type in is not a multiple of 10')

# 7-4
# ingredients = []
# ingredients_typein = '\nPlease type in your ingredients for pizza:'
# ingredients_typein += "\n(When you finish , you can type in 'quit' to close.)"
#
# while True :
# 	ingredient = input(ingredients_typein)
# 	ingredients.append(ingredient)
# 	if ingredient == 'quit':
# 		ingredients.remove('quit')
# 		break
# print('Now we have :',ingredients)

# 7-8
# sandwich_orders = ['Tuna','Beef','Chicken','Pork','Salmon']
# finished_sandwiches = []
# while sandwich_orders:
# 	confirmed_sandwich = sandwich_orders.pop()
# 	finished_sandwiches.append(confirmed_sandwich)
# 	print('\nI made your %s sandwich'%(confirmed_sandwich))
# print('\nThe following sandwiches have already been finished:')
# for sandwich in finished_sandwiches :
# 	print(sandwich)

# 7-9
sandwich_orders = ['Tuna', 'Beef', 'Chicken', 'Pork', 'Salmon', 'Pastrami', 'Pastrami', 'Pastrami']
# print a notice telling everyone that the pastrami has been sold out
print('The pastrami has been sold out right now ')
while 'Pastrami' in sandwich_orders:
	sandwich_orders.remove('Pastrami')
print(sandwich_orders)
