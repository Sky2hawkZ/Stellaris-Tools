import json
import re
import sys
""" 
TODO:
- ✅ Read the generated file from \Documents\Paradox Interactive\Stellaris\logs\script_documentation
- ✅ Filter the Contents of the "script_documentation" file.
	- ✅ Handle tags that have several coinciding categories when filtering
- ✅ Create a dictionary of lists of relevant modifies(value), for each category (key) 
- ✅ Write them properly into a json file.
STAGE 2:
- Upgrade functionality to allow file to be sent into script as a parameter
"""

# print('Hello from python!')
# print(f'First Param: {sys.argv[1]}#')
# print(f'Second param: {sys.argv[2]}#')

categories = set()
result = {}

match_category = re.compile("- ([^,]*), Category: (.*)")

def parse_file(file):
	with open(file) as file:
		count = 0
		for line in file:
			count += 1
			if 'Category' not in line:
				continue
			matches = re.match(match_category, line).groups()
			modifier, match_cat = matches[0], matches[1]
			line_cats = [x.strip() for x in match_cat.split(",")]
			categories.update(set(line_cats))
			#TODO: Break down the "Economic Units" category into further sub categories.
			for line_cat in line_cats:
				if line_cat in result:
					result[line_cat].append(modifier)
				else: 
					result[line_cat] = [modifier]
		# print(count)
		# print(categories)

		#Serialize json
		json_object = json.dumps(result, indent=4)
		with open('modifier_groups.json', 'w') as outfile:
			outfile.write(json_object)

parse_file(
	"C:\\Users\\Hangfish\\Documents\\Paradox Interactive\\Stellaris\\logs\\script_documentation\\modifiers.log")
