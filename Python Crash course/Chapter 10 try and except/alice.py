# filename = 'alice.txt'
#
# try:
# 	with open(filename)as f_obj:
# 		contents = f_obj.read()
# except FileNotFoundError:
# 	msg = 'Sorry , the file ' + "'" + filename + "'" + ' does not exist. '
# 	print(msg)

# title = 'Alice in Wonderland'
# words = title.split()
# print(len(words))

# filename = 'sanguo_utf8.txt'
#
# with open(filename)as f_obj :
# 	words = filename.split()
# 	print(len(words))

# 10-6
# while True:
# 	fst_number = input('Please enter the first number: ')
# 	sec_number = input('Please enter the second number: ')
# 	if fst_number == 'q' or sec_number == 'q':
# 		#if条件判断语句如果为非0或者非空，则都为true，所以这地方不能写数字1 or 数字2 =='q'
# 		break
# 	try:
# 		anwser = int(fst_number) + int(sec_number)
# 	except ValueError:
# 		print('Please enter a valid number,you can try 1,2 or 3.')
# 	else:
# 		print(anwser)

#10-10
filename = 'Animal Carvings.txt'

with open(filename) as f_obj:
	contents = f_obj.read()
	print(contents.lower().count('the'))


