class Node:
    def __init__(self, key, val, left = None, right = None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = dict() # {key : reference to node}
        
        # Initialize front and back nodes, and make the point at each other
        self.back = Node('back', 'back')
        self.front = Node('front', 'front')
        
        self.back.right = self.front
        self.front.left = self.back

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        # Update the node: remove it from the list, and put it at the front
        node = self.cache[key]
        self.removeFromList(node)
        self.insertAtFront(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        # Insert a new node at the front - inbetween the most recently used one and the front node
        if key not in self.cache:
            newNode = Node(key, value)
            self.insertAtFront(newNode)
            self.cache[key] = newNode
        
        # Update the node if it's already here - remove it from the list, and put in at the front
        else:
            node = self.cache[key]
            node.val = value
            self.removeFromList(node)
            self.insertAtFront(node)
        
        # Evict the least recent node if the cap is exceeded
        if len(self.cache) > self.cap:
            self.evict_lru_node()
    
    # Make the most recent node and the front one point at the new node
    def insertAtFront(self, node):
        mostRecentNode = self.front.left
        mostRecentNode.right = node
        self.front.left = node
        node.left = mostRecentNode
        node.right = self.front
    
    # Make the neighboring nodes point at each other
    def removeFromList(self, node):
        node.left.right = node.right
        node.right.left = node.left
    
    def evict_lru_node(self):
        if len(self.cache) > 0:
            leastRecentNode = self.back.right
            self.cache.pop(leastRecentNode.key)
            self.removeFromList(leastRecentNode)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)