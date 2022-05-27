import re
""" 
TODO:
- ✅ Read the generated file from \Documents\Paradox Interactive\Stellaris\logs\script_documentation
- ✅ Filter the Contents of the "script_documentation" file.
	- ✅ Handle tags that have several coinciding categories when filtering
- Create a dictionary of lists of relevant modifies(value), for each category (key) 
- Write them properly into a json file.
"""

categories = set()

# match_category = re.compile(".*Category: (.*)")
match_category = re.compile("- ([^,]*), Category: (.*)")

def parse_file(file):
	with open(file) as file:
		count = 0
		for line in file:
			count += 1
			if 'Category' not in line:
				continue
			# line_cat = [x.strip() for x in re.match(match_category, line).groups()[0].split(",")]
			matches = re.match(match_category, line).groups()
			modifier, match_cat = matches[0], matches[1]
			line_cat = [x.strip() for x in match_cat.split(",")]
			categories.update(set(line_cat))
			print(repr(modifier))
		print(count)
		print(categories)


parse_file(
	"C:\\Users\\Hangfish\\Documents\\Paradox Interactive\\Stellaris\\logs\\script_documentation\\modifiers.log")
