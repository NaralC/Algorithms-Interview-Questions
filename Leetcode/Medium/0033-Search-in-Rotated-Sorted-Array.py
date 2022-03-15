class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Time: O(logn)
        #Space: O(1)
        #Find the pivot of the rotation -> search on the appropriate side
        
        def binarySearch(left, right):
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    return mid
                
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            
            return -1
        
        def findMin(left, right):
            
            while left <= right:
                mid = (left + right) // 2
                
                #Found the minimum
                if nums[mid] > nums[mid + 1]:
                    return mid + 1
                
                #If mid is on on the right sorted side
                if nums[left] > nums[mid]:
                    right = mid - 1
                
                #If mid is on the left sorted side
                else:
                    left = mid + 1
                
        #Edge cases where the input array is already sorted or has a length of 1
        if nums[0] <= nums[-1]:
            return binarySearch(0, len(nums) - 1)
        
        #Find the point where rotation starts, namely the minimum
        pivot = findMin(0, len(nums) - 1)
        
        #Pick a side to search
        if nums[0] > target:
            return binarySearch(pivot, len(nums) - 1)
        else:
            return binarySearch(0, pivot)