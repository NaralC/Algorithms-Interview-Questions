class Solution:
    def rob(self, nums: List[int]) -> int:
        return slidingWindow(nums)

def slidingWindow(nums):
    #Time: O(n)
    #Space: O(1)
    rob1, rob2 = 0, 0
    
    #[rob1, rob2, n, n + 1, ...]
    for house in nums:
        #Rob this house or the previous one
        decision = max(house + rob1, rob2)
        
        #Move both pointers forward
        rob1 = rob2
        rob2 = decision
    
    return rob2 #Since the max amount of cash is decided at the last position
    
        
class Solution:
    def rob(self, nums: List[int]) -> int:
        # Time: O(n)
        # Space: O(n)
        if len(nums) <= 1: return max(nums)

        lookup = [0] * len(nums)
        lookup[0] = nums[0]
        lookup[1] = max(nums[0], nums[1])

        for idx in range(2, len(nums)):
            # Can't rob adjacent: either rob this (along with a non-adjacent house to the left) or just the previous one
            lookup[idx] = max(lookup[idx - 2] + nums[idx], lookup[idx - 1])

        return max(lookup)
