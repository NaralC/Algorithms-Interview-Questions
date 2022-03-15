class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        #Time: O(n)
        #Space: O(1)
        
        output = 0
        
        for element in operations:
            output += 1 if element in {'++X', 'X++'} else -1
                
        return output