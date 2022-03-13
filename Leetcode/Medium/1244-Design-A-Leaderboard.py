class Leaderboard:
    
    def __init__(self):
        #Time: O(1)
        #Space: O(n)
        
        self.table = dict()

    def addScore(self, playerId: int, score: int) -> None:
        #Time: O(1)
        #Space: O(1)
        
        if playerId in self.table:
            self.table[playerId] += score
        else:
            self.table[playerId] = score
        
    def top(self, K: int) -> int:
        #Time: O(nlogn)
        #Space: O(1)
        
        return sum(sorted(self.table.values(), reverse = True)[:K])
            
    def reset(self, playerId: int) -> None:
        #Time: O(1)
        #Space: O(1)
        
        del self.table[playerId]

# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)