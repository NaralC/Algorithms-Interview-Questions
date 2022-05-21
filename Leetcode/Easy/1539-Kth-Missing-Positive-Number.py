class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # Time: O(logn)
        # Space: O(n)
        
        # Binary search
        left = 0
        right = len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            missingCount = arr[mid] - mid - 1 # Find out number of missing positives via index
            
            if missingCount < k:
                left = mid + 1
            else:
                right = mid - 1
        
        return left + k