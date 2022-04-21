from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Time: O(logm) where m = max(piles)
        # Space: O(1)
        # The fastest speed needed is max(piles), as it'd still take an hour on each pile
        # Perform binary search on the range 1, 2, 3, ..., max(piles)
        
        output = float('inf')
        left = 1; right = max(piles)
        
        while left <= right:
            # Calculate the time current speed takes to eat all bananas
            k = (left + right) // 2
            count = 0
            
            for pile in piles:
                count += ceil(pile / k)
            
            # If the current speed is feasible, seek a lower speed
            if count <= h:
                output = min(k, output)
                right = k - 1
            
            # Else find a higher speed
            else:
                left = k + 1
        
        
        return output