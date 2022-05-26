""" 
TODO:
- Read the generated file from \Documents\Paradox Interactive\Stellaris\logs\script_documentation
- Filter the Contents of the "script_documentation" file.
- Create Filtered groups and clusters of modifiers
- Write them properly into a json file.
"""
def parse_file(file):
	with open(file) as file:
		count = 0
		for line in file:
			count += 1
			print(line.rstrip())
		print(count)

parse_file("./3.0.1 modifiers.txt") 