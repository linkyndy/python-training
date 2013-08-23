import collections

def flatten(list_a, list_b, max_depth):
	# Check if the desired depth has been reached
	if max_depth > 0:

		# If it has not, parse each of the two lists and
		# remove a level of recursion; check for each item
		# whether it is a list or an element; flatten the item
		# for the former or append the item for the latter
		new_a = []
		for item in list_a:
			if isinstance(item, collections.Iterable):
				new_a.extend(item)
			else:
				new_a.append(item)

		new_b = []
		for item in list_b:
			if isinstance(item, collections.Iterable):
				new_b.extend(item)
			else:
				new_b.append(item)

		# Go to the next level of recursion
		return flatten(new_a, new_b, max_depth-1)
	else:
		# If it has, return the flattenned lists
		return list_a + list_b

print flatten([1, 2, [3, [4, 5]], 6, [7]], [1, [2], 3], 0)
# Should print: [1, 2, [3, [4, 5]], 6, [7], 1, [2], 3]

print flatten([1, 2, [3, [4, 5]], 6, [7]], [1, [2], 3], 1)
# Should print: [1, 2, 3, [4, 5], 6, 7, 1, 2, 3]

print flatten([1, 2, [3, [4, 5]], 6, [7]], [1, [2], 3], 2)
# SHould print: [1, 2, 3, 4, 5, 6, 7, 1, 2, 3]