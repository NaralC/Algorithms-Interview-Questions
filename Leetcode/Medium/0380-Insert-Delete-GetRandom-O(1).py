from random import randint

class RandomizedSet:

    def __init__(self):
        self.lookup = dict() # { val : its idx in self.list, ... }
        self.list = []

    def insert(self, val: int) -> bool:
        if val not in self.lookup:
            self.lookup[val] = len(self.list)
            self.list.append(val)
            return True
        
        return False

    def remove(self, val: int) -> bool:
        if val in self.lookup:
            # Replace val with the last element of self.list
            top = self.list[-1]
            self.list[self.lookup[val]] = top
            self.lookup[top] = self.lookup[val]
            
            # Remove the last element
            del self.lookup[val]
            self.list.pop()
            return True
        
        return False

    def getRandom(self) -> int:
        return self.list[randint(0, len(self.list) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()