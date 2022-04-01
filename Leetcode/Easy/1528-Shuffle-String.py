class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        # Time: O(n)
        # Space: O(n)
        
        output = [None] * len(s)
        
        for idx, char in zip(indices, s):
            output[idx] = char
            
        return ''.join(output)