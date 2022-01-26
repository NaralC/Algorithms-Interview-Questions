class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        #Time: O(n^2)
        #Space: O(1)
        #Essentially '3Sum' but with a small modification
        
        nums.sort()
        output = nums[0] + nums[1] + nums[2]
        
        for idx in range(len(nums) - 2):
            left, right = idx + 1, len(nums) - 1
            
            while left < right:
                currentSum = nums[idx] + nums[left] + nums[right]
                
                #Modification: check whether the gap between the current sum and target is smaller
                #than that of the previous one
                if abs(currentSum - target) < abs(output - target):
                    output = currentSum
                
                if currentSum > target:
                    right -= 1
                elif currentSum < target:
                    left += 1
                else:
                    return currentSum
        
        return output