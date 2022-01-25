class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        #Time: O(n)
        #Space: O(n)
        
        N = len(s)
        answer = [float('inf') for _ in range(N)]
        
        counter = float('inf')
        for idx in range(N):
            #Run into a c -> reset counter
            if s[idx] == c:
                counter = 0
            #Run into something else -> increment counter
            else:
                counter += 1
            
            answer[idx] = min(answer[idx], counter)
            
        counter = float('inf')
        for idx in reversed(range(N)):
            #Run into a C -> reset counter
            if s[idx] == c:
                counter = 0
            #Run into something else -> increment counter
            else:
                counter += 1
            
            answer[idx] = min(answer[idx], counter)
            
        return answer