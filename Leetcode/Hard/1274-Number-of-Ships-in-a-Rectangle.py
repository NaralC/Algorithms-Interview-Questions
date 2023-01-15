# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        # Time: O(?)
        # Space: O(?)
        
        def quadrantSearch(topRight, botLeft):
            # Boundary breaks or no ships
            if botLeft.x > topRight.x or botLeft.y > topRight.y or not sea.hasShips(topRight, botLeft):
                return 0

            # On 1x1 plane, exactly on top of a ship
            if botLeft.x == topRight.x and botLeft.y == topRight.y:
                return 1
            
            mid_x = (botLeft.x + topRight.x) // 2
            mid_y = (botLeft.y + topRight.y) // 2
            
            topLeftQ = quadrantSearch(Point(mid_x, topRight.y), Point(botLeft.x, mid_y + 1))
            topRightQ = quadrantSearch(topRight, Point(mid_x + 1, mid_y + 1))
            botLeftQ = quadrantSearch(Point(mid_x, mid_y), botLeft)
            botRightQ = quadrantSearch(Point(topRight.x, mid_y), Point(mid_x + 1, botLeft.y))
            
            return topLeftQ + topRightQ + botLeftQ + botRightQ
        
    
        return quadrantSearch(topRight, bottomLeft)
    