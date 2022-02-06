class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        #Time: O(n^2)
        #Space: O(1)
        
        #Flip and invert all rows in one nested loop
        for row in image:
            left, right = 0, len(row) - 1
            
            #<= because we need to take care of the middle element
            while left <= right:
                #^ xor operator inverts the values (look up the truth table)
                row[left], row[right] = row[right] ^ 1, row[left] ^ 1
                
                left += 1; right -= 1
                
        return image