""" 
TODO:
- ✅ Read the generated file from \Documents\Paradox Interactive\Stellaris\logs\script_documentation
- ✅ Filter the Contents of the "script_documentation" file.
- Create a dictionary of lists of relevant modifies(value), for each category (key) 
- Write them properly into a json file.
"""

categories = []

def parse_file(file):
	with open(file) as file:
		count = 0
		current_cat = ""
		for line in file:
			if 'Category' not in line:
				continue
			count += 1
			split_line = line.rstrip().split(',');
			line_cat = split_line[-1].split(': ')[-1].strip()
			if line_cat != current_cat and line_cat not in categories:
				current_cat = line_cat
				categories.append(current_cat)
			# print(current_cat)
			# print(split_line)
			 
		print(count)
		print(categories)


parse_file(
	"C:\\Users\\Hangfish\\Documents\\Paradox Interactive\\Stellaris\\logs\\script_documentation\\modifiers.log")
