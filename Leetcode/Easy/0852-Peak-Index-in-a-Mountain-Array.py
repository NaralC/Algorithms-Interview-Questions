class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        #Time: O(logn)
        #Space: O(1)
        
        left, right = 0, len(arr) - 1
        
        while left < right:
            mid = (left + right) // 2
            candidate = arr[mid]
            
            #Found the peak
            if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
                return mid
            
            #On a descending slope -> look to the left
            elif arr[mid] > arr[mid + 1]:
                right = mid - 1
                
            #On an ascending slope -> look to the right
            else:
                left = mid + 1
            
        return left