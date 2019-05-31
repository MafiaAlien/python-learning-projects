
with open('pi_digits.txt') as file_project:
	contents = file_project.readlines()
	for line in contents:
		line = line.rstrip()
		print(line)

	