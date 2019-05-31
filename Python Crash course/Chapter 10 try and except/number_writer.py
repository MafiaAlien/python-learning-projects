import json

# number = ['1','2','3','4','11','15','23','30']
#
filename = 'number.json'
# with open(filename,'w')as n_obj:
# 	json.dump(number,n_obj)

with open(filename)as n_obj:
	numbers = json.load(n_obj)

print(numbers)
