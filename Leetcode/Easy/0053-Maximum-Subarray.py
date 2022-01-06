class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return kadanesAlgo(nums)
        
def optimized(nums):
    #Time: O(n)
    #Space: O(1)
    
    maxSoFar, maxThisPos = nums[0], nums[0]
    
    for idx in range(1, len(nums)):
        maxThisPos = max(nums[idx], nums[idx] + maxThisPos)
        maxSoFar = max(maxSoFar, maxThisPos)
        
    return maxSoFar
        
def kadanesAlgo(nums):
    #Time: O(n)
    #Space: O(n)
    
    track = [float('-inf') for _ in range(len(nums))]

    for idx in range(len(nums)):
        track[idx] = max(nums[idx], nums[idx] + track[idx - 1])

    return max(track)