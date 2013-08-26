from collections import OrderedDict

def to_dictionaries(file):
	"""Converts a file with a specified format to dictionaries"""
	
	# Holds the list of dictionaries which will be returned
	dicts = []

	# Holds the currently parsed dictionary
	d = {}

	for line in open(file):
		# Start a new dictionary after each empty line; else
		# append key-value pair to current dictionary
		if line == '\n':
			dicts.append(d)
			d = {}
		else:
			key, val = line.split()
			d[key] = val

	dicts.append(d)

	return dicts

def compare(a, b):
	"""Compares dictionary values"""

	av = a.values()
	bv = b.values()

	for i in range(max(len(av), len(bv))):
		return cmp(av[i], bv[i])

def sort_dicts(dict_list):
	"""Sorts a dictionary list by a specified algorithm"""

	# Make each dict an OrderedDict and sort the keys ascending
	for i in range(len(dict_list)):
		dict_list[i] = OrderedDict(sorted(dict_list[i].items(), key=lambda k: k[0]))

	# Sort and return the dict list
	return sorted(dict_list, cmp=compare)

print sort_dicts(to_dictionaries("dicts.txt"))
