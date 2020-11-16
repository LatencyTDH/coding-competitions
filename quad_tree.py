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
        if not grid or not grid[0]:
            return Node()
        n = len(grid)
        return build(grid, 0, n - 1, 0, n - 1)

def build(grid, startr, endr, startc, endc):
    if endr-startr == 0 and endc-startc == 0:
        blip = Node()
        blip.val = grid[startr][startc]
        blip.isLeaf = True
        return blip
    
    n = endr - startr + 1
    midr, midc = startr + (n // 2), startc + (n // 2)
    root = Node(
            '*',
            False,
            build(grid, startr, midr - 1, startc, midc - 1),
            build(grid, startr, midr - 1, midc, endc),
            build(grid, midr, endr, startc, midc - 1),
            build(grid, midr, endr, midc, endc)
    )

    corners = (root.topLeft, root.topRight, root.bottomLeft, root.bottomRight)
    
    if all(c.val == 1 for c in corners) or all(c.val == 0 for c in corners):
        root.val = root.topLeft.val
        root.isLeaf = True
        clear_corner_children(root)
    return root

def clear_corner_children(node):
    node.topLeft = None
    node.topRight = None
    node.bottomLeft = None
    node.bottomRight = None

def construct2(self, grid: 'List[List[int]]') -> 'Node':
    root = Node(True, True, None, None, None, None)
    if len(set([item for row in grid for item in row])) == 1:
        root.val = bool(grid[0][0])
    else:
        root.isLeaf = False
        size = len(grid)
        root.topLeft = self.construct([row[:size//2] for row in grid[:size//2]])
        root.topRight = self.construct([row[size//2:] for row in grid[:size//2]])
        root.bottomLeft = self.construct([row[:size//2] for row in grid[size//2:]])
        root.bottomRight = self.construct([row[size//2:] for row in grid[size//2:]])
    return root