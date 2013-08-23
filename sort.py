def to_dictionary(file):
	"""Converts a file with a specified format to a dictionary"""
	
	d = {}

	for line in open(file):
		key, val = line.split()
		d[key] = val

	return d
