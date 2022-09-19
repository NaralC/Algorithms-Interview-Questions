from collections import defaultdict

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # Time: O(n)
        # Space: O(n)
        
        # Mod everything by 60 first
        time = [num % 60 for num in time]
        
        output = 0
        seen = defaultdict(int)
        
        for num in time:
            diff = (60 - num) % 60
            
            if diff in seen:
                output += seen[diff]
                
            seen[num] += 1
            
        return output
        