def preorder_generator(tree):
	if not tree:
		return
		
	yield tree[0]

	if tree[1] is not None:
		for ltree in preorder_generator(tree[1]):
			yield ltree

	if tree[2] is not None:
		for rtree in preorder_generator(tree[2]):
			yield rtree
