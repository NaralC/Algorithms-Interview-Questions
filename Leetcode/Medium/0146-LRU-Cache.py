class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.lookup = dict() # { key : reference to node }
        
        # Old <-> New
        self.old = Node(float('-inf'), float('-inf'))
        self.new = Node(float('inf'), float('inf'))
        self.old.next = self.new
        self.new.prev = self.old

    def get(self, key: int) -> int:
        if key not in self.lookup:
            return -1
        
        # Remove from middle of list and insert at the front
        self.remove(self.lookup[key])
        self.insert(self.lookup[key])
        return self.lookup[key].val

    def put(self, key: int, value: int) -> None:
        # Remove from middle of list if the node exists
        if key in self.lookup:
            self.remove(self.lookup[key])
        
        # Update the key and value then insert the node to the front
        self.lookup[key] = Node(key, value)
        self.insert(self.lookup[key])
        
        # Evict oldest node should the quota's exceeded
        if len(self.lookup) > self.cap:
            toBeRemoved = self.old.next
            self.remove(toBeRemoved)
            del self.lookup[toBeRemoved.key]
            
    def remove(self, node):
        # Make neighboring nodes point at each other
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
        
    def insert(self, node):
        # Make the 'new' node and the currently newest one point at our node
        prev, nxt = self.new.prev, self.new
        prev.next = node
        node.prev = prev
        nxt.prev = node
        node.next = nxt

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)