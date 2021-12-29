class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #Time: O(logn)
        #Space: O(1)
        
        left, right = 0, len(nums) - 1
        
        #left <= right doesn't work since it can result in idx being out of range
        while left < right:
            mid = (left + right) // 2
            
            #Found the peak
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            #We're on a rising slope, so the peak is to the right
            if nums[mid] < nums[mid + 1]: 
                left = mid + 1
            #We're on a downward slope, so the peak is to the left
            elif nums[mid] > nums[mid - 1]:
                right = mid - 1
        
        #Handles cases where:
        #1) len(nums) == 1, return the only idx
        #2) len(nums) == 2, return the bigger idx
        return left