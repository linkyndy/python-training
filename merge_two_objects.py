def merge_objects(a, b):
	"""Merge two objects up to any depth"""

	while len(a) > 0:
		key, value = a.popitem()

		if key in b:
			if type(value) != type(b[key]):
				b[key] = (value, b[key])
			elif isinstance(value, dict):
				b[key] = merge_objects(value, b[key])
			elif isinstance(value, set):
				b[key] = value.union(b[key])
			else:
				b[key] = value + b[key]
		else:
			b[key] = value

	return b


a = {'x': [1, 2, 3], 'y': 1, 'z': set([1, 2, 3]), 'w': 'qweqwe', 't': {'a': [1, 2]}, 'm': [1]}
b = {'x': [4, 5, 6], 'y': 4, 'z': set([4, 2, 3]), 'w': 'asdf', 't': {'a': [3, 2]}, 'm': "wer"}

print merge_objects(a, b)
# Should print: {'m': ([1], 'wer'), 't': {'a': [1, 2, 3, 2]}, 'w': 'qweqweasdf', 'y': 5, 'x': [1, 2, 3, 4, 5, 6], 'z': set([1, 2, 3, 4])}