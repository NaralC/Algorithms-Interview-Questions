class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        #Time: O(n^2)
        #Space: O(1)
        
        nums.sort()
        count = 0
        
        for idx in range(len(nums)):
            left, right = idx + 1, len(nums) - 1
            
            while left < right:
                currentSum = nums[idx] + nums[left] + nums[right]
                
                #Since the array is sorted, all numbers between left and right will always be less than nums[right] - thus adding up to less than the target
                if currentSum < target:
                    count += right - left
                    left += 1
                
                #We only need values exclusively smaller than target
                else:
                    right -= 1
                    
        return count