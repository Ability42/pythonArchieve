# Tree Representation

# Tree Realized
# >>> T = [["a", "b"], ["c"], ["d", ["e", "f"]]]
# >>> T[0][1]
# <<<'b'
# >>> T[2][1][0]
# <<<'e'

# Example tree with a marked path from the root to leaf
class Tree(object):
	def __init__(self, left, right):
		self.left = left
		self.right = right

# >>> t = Tree(Tree("a", "b"), Tree("c", "d"))
# >>> t.right.left
# <<< 'c'

