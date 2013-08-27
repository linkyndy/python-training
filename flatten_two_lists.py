def flatten_two_lists(a, b, depth):
	"""Flatten two lists up to depth"""

	def flatten(l, depth):
		"""Recursively flatten list up to depth"""

		if isinstance(l, list):
			if depth == 0:
				return l
			if len(l) == 0:
				return []
			
			first, rest = l[0], l[1:]
			return flatten(first, depth - 1) + flatten(rest, depth)
		else:
			return [l]

	return flatten(a, depth), flatten(b, depth)
	
print flatten_two_lists([1, 2, [3, [4, 5]], 6, [7]], [1, [2], 3], 0)
# Should print: [1, 2, [3, [4, 5]], 6, [7], 1, [2], 3]

print flatten_two_lists([1, 2, [3, [4, 5]], 6, [7]], [1, [2], 3], 1)
# Should print: [1, 2, 3, [4, 5], 6, 7, 1, 2, 3]

print flatten_two_lists([1, 2, [3, [4, 5]], 6, [7]], [1, [2], 3], 2)
# SHould print: [1, 2, 3, 4, 5, 6, 7, 1, 2, 3]