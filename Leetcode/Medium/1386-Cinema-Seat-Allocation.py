from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # Time: O(n)
        # Space: O(n)

        # Since allocating seats asymmetrically isn't allowed, we can only sit on seats col-numbered 2-4, 4-7, 6-9
        # Also take the left and right sides first to maximize output
        takenSeats = defaultdict(set)
        
        for row, col in reservedSeats:
            if col in [2, 3, 4, 5]:
                takenSeats[row].add('left')
            
            if col in [4, 5, 6, 7]:
                takenSeats[row].add('middle')

            if col in [6, 7, 8, 9]:
                takenSeats[row].add('right')
                
        # Assuming no seats are predominantly blocked, 2 groups can take the left and right side of n row
        output = 2 * n
        
        # Defaultdict only iterate over existing keys, so this loop only considers non-empty rows
        for row in takenSeats:
            if len(takenSeats[row]) == 3:
                output -= 2 # No groups get to sit
            else:
                output -= 1 # Only one group get to sit
        
        return output