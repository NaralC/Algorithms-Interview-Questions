# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Time: O(logn)
        #Space: O(1)
        
        #Binary Search
        #Case1: found a bad version 👉 look to the left, see if there's any lower bad version
        #Case2: bad version not found 👉 look to the right
        
        left, right = 1, n
        while left <= right:
            middle = (left + right) // 2
            
            if isBadVersion(middle):
                right = middle - 1
            else:
                left = middle + 1
                
        #Returning left covers all edge cases
        return left