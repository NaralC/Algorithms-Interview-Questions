class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #Time: O(n^3)
        #Space: O(1)
        
        nums.sort()
        output = set()
        
        for idx in range(len(nums)):
            for subIdx in range(idx + 1, len(nums)):
                
                left, right = subIdx + 1, len(nums) - 1
                
                while left < right:
                    currentSum = nums[idx] + nums[subIdx] + nums[left] + nums[right]
                    
                    if currentSum < target:
                        left += 1
                    elif currentSum > target:
                        right -= 1
                    else:
                        output.add((nums[idx], nums[subIdx], nums[left], nums[right]))
                        
                        left += 1; right -= 1
                        
        return output