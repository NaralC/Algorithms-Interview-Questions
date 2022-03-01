class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        #Time: O(n)
        #Space: O(n)
        
        output = []
        left, right = 0, len(nums) - 1
        
        while left <= right:
            leftNum, rightNum = pow(nums[left], 2), pow(nums[right], 2)
            
            if leftNum > rightNum:
                output.append(leftNum)
                left += 1
            else:
                output.append(rightNum)
                right -= 1
                
        return output[::-1]