class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #Time: O(n^2)
        #Space: O(n)
        
        #Each number is a sequence of length 1 on its own
        dp = [1 for _ in range(len(nums))]
        
        #Start by looping backwards since the last element is always a sequence of length 1
        for idx in reversed(range(len(nums) - 1)):
            
            #Iterate forward to look for potential increasing sequences
            for subIdx in range(idx + 1, len(nums)):
                if nums[idx] < nums[subIdx]:
                    dp[idx] = max(dp[idx], 1 + dp[subIdx])
                    
        return max(dp)