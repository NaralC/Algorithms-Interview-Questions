from errno import EILSEQ


class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Time: O(logn)
        #Space: O(1)
        
        output = nums[0]
        left, right = 0, len(nums) - 1
        
        while left <= right:
            #Our boundary is exclusively on the smaller sorted side
            if nums[left] < nums[right]:
                return min(output, nums[left])
            
            #Our boundary is not exclusively on the smaller sorted side yet
            else:
                mid = (left + right) // 2
                output = min(output, nums[mid])
                
                #Mid still hangs on the bigger side
                if nums[left] <= nums[mid]:
                    left = mid + 1
                
                #Mid already on the smaller side
                else:
                    right = mid - 1
        
        return output