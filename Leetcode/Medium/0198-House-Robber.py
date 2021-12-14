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
    
        
def memoization(nums):
    #Time: O(n)
    #Space: O(n)
    dp = [0] * len(nums)

    for idx, num in enumerate(nums):
        if idx < 2:
            dp[idx] = num
        else:
            dp[idx] = num + max(dp[idx - 2], dp[idx - 3])

    return max(dp)