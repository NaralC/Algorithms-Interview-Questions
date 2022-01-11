class Solution:
    def maxArea(self, height: List[int]) -> int:
        return optimized(height)
    
def optimized(height):
    #Time: O(n)
    #Space: O(1)
    maxArea = 0
    left, right = 0, len(height) - 1
    
    while left < right:
        currentArea = min(height[left], height[right]) * (right - left)
        maxArea = max(maxArea, currentArea)
        
        #Case1: move the left ptr if its value is smaller (in hopes of finding a bigger value)
        if height[left] < height[right]:
            left += 1
        
        #Case2: move the right ptr if its value is smaller (in hopes of finding a bigger value)
        elif height[left] > height[right]:
            right -= 1
        
        #Case3: left == right, move either
        else:
            left +=  1
            
    return maxArea

def bruteForce(height):
    #Time: O(n^2)
    #Space: O(n)
    
    maxArea = 0
    for start in range(len(height)):
        for end in range(start + 1, len(height)):
            area = min(height[start], height[end]) * (end - start)
            maxArea = max(maxArea, area)
            
    return maxArea