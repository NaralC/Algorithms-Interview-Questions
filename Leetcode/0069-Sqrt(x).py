class Solution:
    def mySqrt(self, target: int) -> int:
        #Time: O(n)
        #Space: O(1)
        start = 0
        end = target
        
        while start <= end:
            middle = (start + end) // 2
            candidate = middle * middle
            
            if candidate == target:
                return middle
            elif candidate > target:
                end = middle - 1
            else:
                start = middle + 1
        
        return start - 1