from heapq import *
from collections import defaultdict

class Leaderboard:
    # Time: O(klogk + k)
    # Space: O(n + k)
    
    def __init__(self):
        # Time: O(1)
        # Space: O(n)
        
        self.board = defaultdict(int)
        
    def addScore(self, playerId: int, score: int) -> None:
        # Time: O(1)
        # Space: O(1)
        
        self.board[playerId] += score
        
    def top(self, k: int) -> int:
        # Time: O(klogk + k)
        # Space: O(k)
        
        minHeap = []
        
        for score in self.board.values():
            heappush(minHeap, score)
            
            if len(minHeap) > k: heappop(minHeap)
        
        return sum(score for score in minHeap)
        
    def reset(self, playerId: int) -> None:
        # Time: O(1)
        # Space: O(1)
        
        self.board[playerId] = 0
        
# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)