class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.key_map = {}
        self.capacity = capacity
        self.head = None
        self.tail = None
    
    def _push_front(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        
        old_head = self.head
        tail = self.tail
        old_head.prev = node
        node.next = old_head
        node.prev = tail
        tail.next = node
        
        # Reassign head pointer of DLL to the added node
        self.head = node
    
    def _remove_last(self):
        return self._remove_node_from_list(self.tail)
    
    def _remove_node_from_list(self, node):
        # Returns the key of the removed node
        k = node.key
        rem_ref = self.key_map[k]
        
        if rem_ref == self.head and rem_ref == self.tail:
            self.head = None
            self.tail = None
        elif rem_ref == self.head:
            self.tail.next = rem_ref.next
            self.head = self.tail.next
            self.head.prev = self.tail
        elif rem_ref == self.tail:
            self.head.prev = self.tail.prev
            self.tail = self.head.prev
            self.tail.next = self.head
        else:
            prev_node = rem_ref.prev
            next_node = rem_ref.next
            prev_node.next = next_node
            next_node.prev = prev_node
        
        return k
        
    def get(self, key: int) -> int:
        if key not in self.key_map:
            return -1
        else:
            node_ref = self.key_map[key]
            self._move_to_front(node_ref)
            return node_ref.val  

    def put(self, key: int, value: int) -> None:
        if key not in self.key_map:
            if len(self.key_map) >= self.capacity:
                removed_key = self._remove_last()
                del self.key_map[removed_key]
            
            node_entry = Node(key, value)
            self._push_front(node_entry)
            self.key_map[key] = node_entry
        else:
            node_ref = self.key_map[key]
            node_ref.val = value
            self._move_to_front(node_ref)

    def _move_to_front(self, node):
        self._remove_node_from_list(node)
        self._push_front(node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)