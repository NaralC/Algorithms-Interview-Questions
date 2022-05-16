class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # Time: O(n * log(m)) where n = len(nums), m = max possible sum of an array
        # Space: O(1)
        
        left = 1
        right = 10000 # Since there're at most 100 elements, each being 100 maximum
        
        while left <= right:
            startVal = (left + right) // 2
            
            # Check if it dips below 1 at any point
            runningSum = startVal
            valid = True
            
            for num in nums:
                runningSum += num
                
                if runningSum < 1:
                    valid = False
                    break
            
            # If the current number works, seek a lower one
            if valid:
                right = startVal - 1
            
            # If the current number doesn't work, seek a higher one
            else:
                left = startVal + 1
                
        return left