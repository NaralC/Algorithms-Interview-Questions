class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Time: O(n)
        # Space: O(1)
        
        window = sum(nums[:k]) # Holds the sum of current numbers in the sliding window
        maxAvg = window / k
        
        for idx in range(k, len(nums)):
            # Remove the left most element
            window -= nums[idx - k]
            
            # Add a new element
            window += nums[idx]
            
            # Update output
            maxAvg = max(maxAvg, window / k) 
            
        return maxAvg