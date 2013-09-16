from itertools import chain, combinations, imap

def subset_generator(s):
	"""Generates powerset of given set
	set([1, 2]) => [set([]), set([1]), set([2]), set([1, 2])]
	"""

	subsets = chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
	for subset in subsets:
		yield set(subset)
