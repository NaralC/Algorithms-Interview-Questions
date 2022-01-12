class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #Time: O(log n)
        #Space: O(1)
        
        #Modified binary search
        #First search: find the first occurence
        #Second search: find the last occurence
        
        def binarySearch(find):
            idx = -1
            left, right = 0, len(nums) - 1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    idx = mid
                    
                    if find == 'first': #look to the left, scan for the first occurence 👈
                        right = mid - 1
                    elif find == 'last': #look to the right, scan for the last occurence 👉
                        left = mid + 1
            
            return idx
        
        return [binarySearch('first'), binarySearch('last')]