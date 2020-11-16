class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
    	l = self.left.val if self.left else None
    	r = self.right.val if self.right else None
    	return f"Node: {self.val}, Left: {l}, Right: {r}"
