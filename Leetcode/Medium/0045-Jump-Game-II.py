class Solution:
    def jump(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        
        output = furthest = 0
        
        while furthest < len(nums) - 1:
            output += 1 # Increment every time we make a jump
            
            # Find the furthest position we can jump to
            leap = 0
            for start in range(furthest + 1):
                leap = max(leap, start + nums[start])
            
            # Update the furthest position we can reach
            furthest = max(furthest, leap)
        
        return output