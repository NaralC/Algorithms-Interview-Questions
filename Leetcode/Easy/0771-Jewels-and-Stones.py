class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        #Time: O(j + s) comes from creating the hashset and looping through stones
        #Space: O(j)
        
        jewels = set(jewels)
        count = 0
        
        for char in stones:
            if char in jewels:
                count += 1
        
        return count