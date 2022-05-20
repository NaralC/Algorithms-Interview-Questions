class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        # Time: O(n)
        # Space: O(1)
        
        # Numbers that look the same when upside down: 0, 1, 6, 8, 9
        rotated = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        
        left = 0; right = len(num) - 1
        
        while left <= right:
            # if the rotated number isn't identical to the orignal, terminate
            if (num[left] not in rotated or num[left] not in rotated or
               rotated[num[left]] != num[right]):
                return False
            
            left += 1; right -= 1
        
        return True