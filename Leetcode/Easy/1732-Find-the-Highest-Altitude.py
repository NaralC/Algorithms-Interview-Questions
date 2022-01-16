class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        #Time: O(n)
        #Space: O(1)
        
        current = 0
        highest = 0
        
        for point in gain:
            current += point
            highest = max(highest, current)
            
        return highest