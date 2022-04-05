class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Time: O(n^2)
        # Space: O(n)
        
        output = set()
        nums.sort()
        
        for idx in range(len(nums)):
            left, right = idx + 1, len(nums) - 1
            
            while left < right:
                current = nums[left] + nums[right] + nums[idx]
                
                if current > 0:
                    right -= 1
                elif current < 0:
                    left += 1
                else:
                    output.add((nums[idx], nums[left], nums[right]))
                    left += 1; right -= 1
            
        return output