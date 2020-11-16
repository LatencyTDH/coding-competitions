from heapq import heappush, heappop, heapify

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        heapify(intervals)
        
        merged = []
        while intervals:
            intv1 = heappop(intervals)
            intv2 = None
            if intervals:
                intv2 = heappop(intervals)
            if intv2 is None:
                merged.append(intv1)
            else:
                if does_overlap(intv1, intv2):
                    merged_intv = [min(intv1, intv2)[0], 
                                   max(intv1, intv2, key=lambda x: x[1])[1]]
                    heappush(intervals, merged_intv)
                else:
                    merged.append(intv1)
                    heappush(intervals, intv2)
                
        return merged

def does_overlap(interval_a, interval_b):
    a, b = interval_a
    c, d = interval_b
    return a <= c <= b or c <= a <= d