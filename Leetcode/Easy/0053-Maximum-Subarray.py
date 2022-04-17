class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return dp(nums)

def dp(nums):
    # Time: O(n)
    # Space: O(n)
    
    runningSum = [float('-inf')] * len(nums)
        
    # At each position, decide whether the number should be by itself or added to the previously running sum
    for idx, num in enumerate(nums):
        runningSum[idx] = max(num, num + runningSum[idx - 1])

    return max(runningSum)
    
def kadanesAlgo(nums):
    # Time: O(n)
    # Space: O(1)
    # Kadane's Algorithm: decide whether the next number should be by itself or added to the running sum

    maxSum = runningSum = nums[0]
        
    for num in nums[1:]:
        runningSum = max(num, num + runningSum)
        maxSum = max(maxSum, runningSum)

    return maxSum
