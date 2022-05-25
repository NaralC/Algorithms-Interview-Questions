class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        # Time: O(nlogn)
        # Space: O(n)
        
        # Get the timestamp down
        timestamp = []
        
        for birth, death in logs:
            timestamp.append((birth, 1))
            timestamp.append((death, -1))
                   
        # Run through the timestamp
        yr = float('inf') # Earliest year with highest population
        curr = hi = 0 # Current and highest population of all time
        
        for year, change in sorted(timestamp):
            # Update population
            curr += change
            
            # Update all time high population and year if the current exceeds it
            if curr > hi:
                hi = curr
                yr = year
            
        return yr