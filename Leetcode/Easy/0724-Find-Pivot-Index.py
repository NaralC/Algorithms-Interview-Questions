class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        #Time: O(n)
        #Space: O(1)
        
        fromLeft, fromRight = 0, sum(nums)
        
        for idx in range(len(nums)):
            if fromLeft == fromRight - nums[idx]:
                return idx
            
            fromLeft += nums[idx]
            fromRight -= nums[idx]
             
        return -1


# class Solution:
#     def pivotIndex(self, nums: List[int]) -> int:
#         #Time: O(n)
#         #Space: O(n)
        
#         N = len(nums)
#         fromLeft = [None for _ in range(N)]
#         fromRight = [None for _ in range(N)]
        
#         current = 0
#         for idx in range(N):
#             current += nums[idx]
#             fromLeft[idx] = current
        
#         current = 0
#         for idx in reversed(range(N)):
#             current += nums[idx]
#             fromRight[idx] = current
        
#         for idx in range(N):
#             if idx == 0 and fromRight[idx + 1] == 0:
#                 return idx
            
#             elif idx == N - 1 and fromLeft[idx - 1] == 0:
#                 return idx
            
#             elif idx > 0 and idx < N - 1 and fromLeft[idx - 1] == fromRight[idx + 1]:
#                 return idx
        
#         return -1   