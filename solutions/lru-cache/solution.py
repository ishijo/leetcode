class Node:
    def __init__(self, key=0, val=0):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class LRUCache: 

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head,self.tail = Node(),Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def update_MRU(self,node):
        old_MRU = self.tail.prev

        self.tail.prev = node ## link
        node.next = self.tail

        node.prev = old_MRU ## link
        old_MRU.next = node

    def remove_LRU(self):
        old_LRU = self.head.next ## link
        new_LRU = old_LRU.next
        self.head.next = new_LRU ## link
        new_LRU.prev = self.head
        del self.cache[old_LRU.key]
    
    def remove(self,node):
        prev_node = node.prev
        old_next_node = node.next
        prev_node.next = old_next_node
        old_next_node.prev = prev_node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.update_MRU(node)
        return node.val

    def put(self, key: int, value: int) -> None:

        if key not in self.cache:
            
            self.cache[key] = Node(key,value)
            node = self.cache[key]
            self.update_MRU(node)

            if len(self.cache)>self.capacity:
                self.remove_LRU()
            

        elif key in self.cache:
            old_node = self.cache[key]
            self.remove(old_node)
            self.cache[key] = Node(key,value)
            node = self.cache[key]
            self.update_MRU(node)
            



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)