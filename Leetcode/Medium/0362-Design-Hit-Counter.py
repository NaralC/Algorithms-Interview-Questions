from collections import deque

class HitCounter:
    # Time: O(n)
    # Space: O(n)
    
    def __init__(self):
        self.q = deque()

    def hit(self, timestamp: int) -> None:
        self.q.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        # Keep shaving off the front until it's within the 5-min boundary
        while len(self.q) and self.q[0] <= timestamp - 300:
            self.q.popleft()
            
        return len(self.q)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)