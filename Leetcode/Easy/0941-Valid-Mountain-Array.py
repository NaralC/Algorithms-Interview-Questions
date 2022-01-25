class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        #Time: O(n)
        #Space: O(1)
        
        #Have two pointers climb based on these conditions:
        #Move up left ptr if it's on ascending slope
        #Move up right ptr if it's on descending slope
        #If there's only one peak - they'll meet in the middle
        
        left, right = 0, len(arr) - 1
        while left < right:
            #Left ptr climb up
            if arr[left] < arr[left + 1]:
                left += 1
            
            #Right ptr climb up
            elif arr[right - 1] > arr[right]:
                right -= 1
            
            #On a flat surface / Neither ascending nor descending
            else:
                break
        
        #Handle cases where it's strictly an uphill/downhill
        if left == 0 or right == len(arr) - 1:
            return False
        
        return left == right