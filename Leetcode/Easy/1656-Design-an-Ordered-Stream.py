class OrderedStream:

    def __init__(self, n: int):
        self.arr = [None] * n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.arr[idKey - 1] = value
        
        output = []
        
        while self.ptr < len(self.arr) and self.arr[self.ptr]:
            output.append(self.arr[self.ptr])
            self.ptr += 1
        
        return output

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value) 