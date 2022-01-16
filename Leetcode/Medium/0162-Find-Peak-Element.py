class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #Time: O(logn)
        #Space: O(1)
        
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            #Case1: found a local peak
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid

            #Case2: go right if the value on that side is bigger
            elif nums[mid] < nums[mid + 1]:
                left = mid + 1
            
            #Case3: go left if the value on that side is bigger
            elif nums[mid] > nums[mid + 1]:
                right = mid - 1
            
            
        #Handle cases where:
        #len(nums) <= 2: return the bigger/only element
        #The input is a slope without spikes
        return left