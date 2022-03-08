class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        #Time: O(n)
        #Space: O(n)
        
        start, end = rounds[0], rounds[-1]
        
        if start <= end:
            return [idx for idx in range(start, end + 1)]
    
        else:
            output = []
            
            for idx in range(1, end + 1):
                output.append(idx)
            
            for idx in range(start, n + 1):
                output.append(idx)
            
            return output