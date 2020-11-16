class Element(object):
    def __init__(self):
        self.parent = self
        self.rank = 1
    
class UnionFindDynamic(object):
    def __init__(self):
        self.items = {}
    
    def make_set(self, val):
        if val not in self.items:
            self.items[val] = Element()
    
    def has(self, key):
        return key in self.items
    
    def union(self, x, y):
        p = self.find(x)
        q = self.find(y)
        if p != q:
            if p.rank < q.rank:
                p.parent = q
            elif q.rank < p.rank:
                q.parent = p
            else:
                q.parent = p
                p.rank += 1
            
    def find(self, x):
        y = self.items.get(x)
        if y is None:
            return None
        return self._find(y)
    
    def _find(self, x):
        if x.parent != x:
            x.parent = self._find(x.parent)
        return x.parent

class UnionFind(object):
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [0] * n
    
    def union(self, x, y):
        p = self.find(x)
        q = self.find(y)
        if p == q:
            return False
        elif self.ranks[p] < self.ranks[q]:
            self.parents[p] = q
        elif self.ranks[q] < self.ranks[p]:
            self.parents[q] = p
        else:
            self.parents[p] = q
            self.ranks[q] += 1
        return True
    
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]