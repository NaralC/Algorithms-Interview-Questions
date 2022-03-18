class MovingAverage:
    #Time: O(1)
    #Space: O(size)
    
    from collections import deque
    
    def __init__(self, size: int):
        self.q = deque()
        self.total = 0
        self.size = size

    def next(self, val: int) -> float:
        self.total += val
        self.q.append(val)
        
        if len(self.q) > self.size:
            self.total -= self.q.popleft()
        
        return self.total / len(self.q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)