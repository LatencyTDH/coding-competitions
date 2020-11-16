# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 1 - 2 - 3 - 4 - 5

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        return self._recurse(head, None)

    def find_middle(self, left: ListNode, right: ListNode) -> ListNode:
        slow = left
        fast = left
        
        while fast and fast.next:
            if fast == right or fast.next == right:
                return slow
            slow = slow.next
            fast = fast.next.next
        
        return slow

    def _recurse(self, head: ListNode, last: ListNode):
        if head == last:
            return None
        
        middle = self.find_middle(head, last)
        node = TreeNode(middle.val)
        node.left = self._recurse(head, middle)
        node.right = self._recurse(middle.next, last)
        return node