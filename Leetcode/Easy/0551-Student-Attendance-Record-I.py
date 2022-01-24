class Solution:
    def checkRecord(self, s: str) -> bool:
        #Time:O(n)
        #Space: O(1)
        
        absent = 0
        late = 0
        
        for char in s:
            if char == 'L':
                late += 1
                if late >= 3: return False
                
            elif char == 'A':
                absent += 1
                late = 0
                
            else:
                late = 0
        
        return True if absent < 2 else False