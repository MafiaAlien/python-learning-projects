with open('pi_digits.txt') as file_project:
	contents = file_project.readlines()

pi_string = ''
for line in contents:
	pi_string += line.strip()

print(pi_string)
print(len(pi_string))
