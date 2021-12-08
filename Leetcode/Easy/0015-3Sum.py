class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Time: O(n^2)
        #Space: O(n)
        nums.sort()
        output = []
        
        #With 3 ptrs, we don't need to check the last 2 elements
        for idx in range(len(nums) - 2):
            #Avoiding duplicates
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            
            start = idx + 1
            end = len(nums) - 1
            
            while start < end:
                currentSum = nums[idx] + nums[start] + nums[end]
                
                if currentSum > 0: #end = end << 1 to decrement sum
                    end -= 1
                elif currentSum < 0: #start = start >> 1 to increment sum
                    start += 1
                else:
                    output.append([nums[idx], nums[start], nums[end]])
                    
                    #Avoiding duplicates
                    start += 1
                    while nums[start] == nums[start - 1] and start < end:
                        start += 1
                    
        return output