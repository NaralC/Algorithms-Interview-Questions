class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # Time: O(nm)
        # Space: O(nm)
        
        #   1 2 3 2 1
        # 3     1   
        # 2   1   2  
        # 1 1       3
        # 4
        # 7
        
        dp = [[0 for _ in range(len(nums2) + 1)] for _ in range(len(nums1) + 1)]
        
        for idx1 in range(len(nums1)):
            for idx2 in range(len(nums2)):
                if nums1[idx1] == nums2[idx2]:
                    if idx1 > 0 and idx2 > 0:
                        dp[idx1][idx2] += dp[idx1 - 1][idx2 - 1] + 1
                    
                    else:
                        dp[idx1][idx2] += 1
        
        return max(max(row) for row in dp)