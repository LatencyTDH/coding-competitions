"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        if not grid:
            return None
        
        n = len(grid)
        leaves = [Node(False, True, None, None, None, None),
                  Node(True, True, None, None, None, None)]
        
        def build_tree(top, left, size) -> 'Node':
            val = grid[top][left]
            
            if any(grid[y][x] != val 
                   for y in range(top, top + size) \
                   for x in range(left, left + size)):
                size //= 2
                
                return Node(False, False,
                            build_tree(top, left, size),
                            build_tree(top, left + size, size),
                            build_tree(top + size, left, size),
                            build_tree(top + size, left + size, size))
            
            return leaves[grid[top][left]]
        
        return build_tree(0, 0, n)