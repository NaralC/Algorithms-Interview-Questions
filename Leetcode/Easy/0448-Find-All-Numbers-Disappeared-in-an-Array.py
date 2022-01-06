class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return optimized(nums)
    
def optimized(nums):
    #Time: O(n)
    #Space: O(1) excluding the output list
    
    nums.insert(0, 0)
    
    for idx in range(1, len(nums)):
        editIdx = abs(nums[idx])
        nums[editIdx] = -1 * abs(nums[editIdx])
    
    output = []
    for idx in range(1, len(nums)):
        if val := nums[idx] > -1:
                output.append(idx)
    
    return output

def extraArray(nums):
    #Time: O(n)
    #Space: O(n)
    
    track = [False for _ in range(len(nums) + 1)]
    
    for num in nums:
        track[num] = True
    
    output = []
    for idx in range(1, len(track)):
        if not track[idx]:
            output.append(idx)
    
    return output