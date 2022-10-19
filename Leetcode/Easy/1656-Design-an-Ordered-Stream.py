class OrderedStream:
    # Time: O(n)
    # Space: O(n)
    
    def __init__(self, n: int):
        self.order = ['' for _ in range(n)]
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.order[idKey - 1] = value
        output = []
        
        while self.ptr < len(self.order):
            if not self.order[self.ptr]:
                break
                
            output.append(self.order[self.ptr])
            self.ptr += 1
        
        return output

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)