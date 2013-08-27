from collections import OrderedDict

def to_dictionaries(file):
	"""Converts a file with a specified format to dictionaries"""
	
	# Holds the list of dictionaries which will be returned
	dicts = []

	# Holds the dictionary ids corresponding to their object id
	ids = {}

	# Holds the current dictionary id
	dict_id = 1

	# Holds the currently parsed dictionary
	d = {}

	for line in open(file):
		# Start a new dictionary after each empty line; else
		# append key-value pair to current dictionary
		if line == '\n':
			dicts.append(d)
			ids[id(d)] = dict_id
			dict_id += 1
			d = {}
		else:
			key, val = line.split()
			d[key] = val

	dicts.append(d)
	ids[id(d)] = dict_id

	return (dicts, ids)

def compare(a, b):
	"""Compares dictionary values"""

	# Get the two dictionaries' values
	av = a.values()
	bv = b.values()

	# Compare values present in both dictionaries; if
	# elements differ, return their compared values
	for i in range(min(len(av), len(bv))):
		if av[i] != bv[i]:
			return cmp(av[i], bv[i])

	# Should reach this line only if all values present in both
	# dictionaries are equal between them; in this case, the 
	# dictionary with fewer elements is the smallest one
	return 1 if len(av) > len(bv) else -1

def sort_dicts(dict_list, ids):
	"""Sorts a dictionary list by a specified algorithm"""

	# Make each dict an OrderedDict and sort the keys ascending
	for i in range(len(dict_list)):
		dict_list[i] = OrderedDict(sorted(dict_list[i].items(), key=lambda k: k[0]))

	# Holds the dict ids that will be returned
	dict_ids = []

	# Sort and parse the sorted dict list
	for d in sorted(dict_list, cmp=compare):
		dict_ids.append(ids[id(d)])

	return dict_ids

def to_file(dict_ids):
	"""Writes a list of dictionary ids to a file"""

	f = open("ids.txt", "w")

	for dict_id in dict_ids:
		f.write("%s " % dict_id)

print to_file(sort_dicts(*to_dictionaries("dicts.txt")))
