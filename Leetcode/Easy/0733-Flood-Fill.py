class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        #Time: O(m*n)
        #Space: O(m*n)
        
        sourceColor = image[sr][sc]
        fill(image, sr, sc, newColor, sourceColor)
        return image
    
def fill(image, row, col, newColor, sourceColor):
    #Prevent boundary break
    if row < 0 or col < 0 or row >= len(image) or col >= len(image[row]):
        return
    
    #Only fill spots with the same source color / Prevent repeated work
    if image[row][col] != sourceColor or image[row][col] == newColor:
        return
    
    #Fill the current spot
    image[row][col] = newColor
    
    #Fill its neighbors
    fill(image, row - 1, col, newColor, sourceColor)
    fill(image, row, col - 1, newColor, sourceColor)
    fill(image, row + 1, col, newColor, sourceColor)
    fill(image, row, col + 1, newColor, sourceColor)