def merge_objects(a, b):
	"""Merge objects regardless their depth"""
	
	# Store merged objects in new object
	new = {}

	# Build a set of merged object keys
	keys = set(a.keys() + b.keys())

	# For each key in the set
	for key in keys:
		# If key is not present in both objects
		# add the existing one to the new object
		if key not in b:
			new[key] = a[key]
		elif key not in a:
			new[key] = b[key]
		else:
			# If key is present in both objects, check the
			# values' type; if it is different, build a tuple
			# out of these values
			if type(a[key]) != type(b[key]):
				new[key] = (a[key], b[key])
			else:
				# Otherwise, values are of the same type; If
				# they are objects, call this function
				# recursively on these objects
				if isinstance(a[key], dict):
					new[key] = merge_objects(a[key], b[key])
				else:
					# Otherwise, the values are not objects; merge
					# them but be aware that if they are sets, a
					# special case should be treated
					if isinstance(a[key], set):
						new[key] = a[key].union(b[key])
					else:
						new[key] = a[key] + b[key]

	# Returned the merged object
	return new

a = {'x': [1, 2, 3], 'y': 1, 'z': set([1, 2, 3]), 'w': 'qweqwe', 't': {'a': [1, 2]}, 'm': [1]}
b = {'x': [4, 5, 6], 'y': 4, 'z': set([4, 2, 3]), 'w': 'asdf', 't': {'a': [3, 2]}, 'm': "wer"}

print merge_objects(a, b)
# Should print: {'m': ([1], 'wer'), 't': {'a': [1, 2, 3, 2]}, 'w': 'qweqweasdf', 'y': 5, 'x': [1, 2, 3, 4, 5, 6], 'z': set([1, 2, 3, 4])}