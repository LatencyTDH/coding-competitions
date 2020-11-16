from collections import deque, defaultdict

class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        bundle = preprocess(org, seqs)
        if bundle is None:
            return False
        adjs = bundle['adjs']
        refcounts = bundle['refs']
        removed_count = 0

        queue = deque([num for num in refcounts if refcounts[num] == 0])
        while queue:
            curr = queue.popleft()
            removed_count += 1
            if queue:
                return False
            for neighbor in adjs[curr]:
                refcounts[neighbor] -= 1
                if refcounts[neighbor] == 0:
                    queue.append(neighbor)
        
        return removed_count == len(org)

def preprocess(org, seqs):
    refcounts = {num:0 for num in org}
    adjs = defaultdict(set)
    distinct_elems = set([])
    
    for seq in seqs:
        prev = None
        for elem in seq:
            if elem not in refcounts:
                return None
            if prev is not None:
                if elem not in adjs[prev]:
                    refcounts[elem] += 1
                adjs[prev].add(elem)
            prev = elem
            distinct_elems.add(elem)
    
    if set(org) != distinct_elems:
        return None
    
    return { 'adjs': adjs, 'refs': refcounts }

# if __name__ == "__main__":
#     sr = Solution().sequenceReconstruction
#     assert sr([4,1,5,2,6,3], [[5,2,6,3],[4,1,5,2]])
#     assert not sr([1,2,3], [[1,2],[1,3]])
#     assert not sr([1,2,3], [[1,2]])
#     assert not sr([1,2], [[1,2],[2,3]])
#     assert sr([1,2,3], [[1,2],[1,3],[2,3]])
#     assert sr([4,1,5,2,6,3], [[5,2,6,3],[4,1,5,2]])
#     assert not sr([1], [])
#     assert not sr([1], [[1,1]])
#     assert sr([1], [[1]])
#     assert sr([1], [[1], [1], [1]])
#     assert not sr([1], [[], []])
