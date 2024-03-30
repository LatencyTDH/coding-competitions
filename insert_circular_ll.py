# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def is_insertion_place(self, head: Node, insert_val: int) -> bool:
        is_cliff_insert = head.val > head.next.val and (
            insert_val >= head.val or insert_val <= head.next.val
        )

        return is_cliff_insert or (head.val <= insert_val <= head.next.val)

    def insert(self, head: Node, insert_val: int) -> Node:
        if head is None:
            curr = Node(insert_val)
            curr.next = curr
            return curr

        curr = head
        while curr.next != head and not self.is_insertion_place(curr, insert_val):
            curr = curr.next

        to_insert = Node(insert_val)
        to_insert.next = curr.next
        curr.next = to_insert
        return head