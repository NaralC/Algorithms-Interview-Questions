class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        #Time: O(n)
        #Space: O(n)
        
        output = []
        maxHeight = float('-inf')
        
        for idx in reversed(range(len(heights))):
            currentHeight = heights[idx]
            
            if currentHeight > maxHeight:
                output.append(idx)
                maxHeight = currentHeight
        
        return output[::-1]