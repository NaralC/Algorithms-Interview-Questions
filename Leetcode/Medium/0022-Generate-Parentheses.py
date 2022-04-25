class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Time: O(2^n)
        # Space: O(2^n)
        
        # Two decisions at each point: append '(' or ')'
        # n = n opening & n closing parentheses
        
        def dfs(opening, closing, current):
            # Terminate invalid cases:
            # 1) A string either has more closings and openings
            # 2) Either count of '(' or ')' exceeds the quota
            if closing > opening or opening > n or closing > n:
                return
            
            # Well-formed parentheses
            if opening == closing == n:
                output.append(''.join(current))
                return
            
            # Continue DFS
            dfs(opening + 1, closing, current + ['(']) # Append '('
            dfs(opening, closing + 1, current + [')']) # Append ')'
        
        output = []
        dfs(0, 0, [])
        return output
    