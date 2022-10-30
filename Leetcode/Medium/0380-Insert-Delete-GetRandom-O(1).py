import random

class RandomizedSet:
    # Time: O(1)
    # Space: O(n)
    
    def __init__(self):
        self.lookup = dict() # { number : its idx in self.arr, ... }
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.lookup:
            return False
        
        self.lookup[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.lookup:
            # Replace val with the last element of self.arr
            top, top_idx = self.arr[-1], self.lookup[val]
            self.arr[top_idx] = top
            self.lookup[top] = self.lookup[val]
            
            # Delete the last element
            self.arr.pop()
            del self.lookup[val]
            return True
        
        return False
    
    def getRandom(self) -> int:
        return self.arr[random.randint(0, len(self.arr) - 1)]    
    

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()