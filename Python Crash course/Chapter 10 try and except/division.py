# try:
# 	print(5/0)
# except ZeroDivisionError:
# 	print('You cannot divide by zero')

print('Give me two numbers, and I will divide them')
print("Enter 'q' to quit.")

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break
	second_number = input("Second number: ")
	try:
		anwser = int(first_number) / int(second_number)
	except ZeroDivisionError:
		print('You cannot divide by zero')
	else:
		print(anwser)
