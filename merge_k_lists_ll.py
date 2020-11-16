# import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # def mergeKLists1(self, lists: List[ListNode]) -> ListNode:
    #     if not lists:
    #         return []
    #     merged = []
    #     k = len(lists)
    #     stage = []
    #     heads = [None] * k
    #     for arr_idx, node in enumerate(lists):
    #         if node:
    #             heads[arr_idx] = node
    #             heapq.heappush(stage, (node.val, arr_idx))
    #     while stage:
    #         val, arr_idx = heapq.heappop(stage)
    #         merged.append(val)
    #         next_node = heads[arr_idx].next
    #         if next_node is not None:
    #             heads[arr_idx] = next_node
    #             heapq.heappush(stage, (next_node.val, arr_idx))
    #     return merged
    
#     def mergeKLists_recursive(self, lists: List[ListNode]) -> ListNode:
#         if not lists:
#             return []
#         elif len(lists) == 1:
#             return lists[0]
#         elif len(lists) == 2:
#             return merge(lists[0], lists[1])
        
#         mid = len(lists) // 2
#         return merge(self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:]))
    
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        n = len(lists)
        end = n - 1
        jump_by = (n + 1) // 2
        while end > 0:
            for i in range(jump_by):
                if i + jump_by <= end: 
                    lists[i] = merge(lists[i], lists[i+jump_by])
                elif i < end:
                    lists[i] = merge(lists[i], None)
            end //= 2
            jump_by = (jump_by + 1) // 2
            
        return lists[0] if lists else []

def merge(a, b):
    dummy = ListNode(None)
    prev = dummy
    while a and b:
        if a.val <= b.val:
            prev.next = a
            a = a.next
        else:
            prev.next = b
            b = b.next
        prev = prev.next
    
    prev.next = a if a is not None else b
    return dummy.next