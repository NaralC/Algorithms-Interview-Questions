class Solution:
    def countBits(self, n: int) -> List[int]:
        #Time: O(n)
        #Space: O(n)
        history = [0 for _ in range(n + 1)]
        most_significant_bit = 1
        
        for idx in range(1, n + 1):
            if most_significant_bit * 2 == idx:
                most_significant_bit = idx
            history[idx] = 1 + history[idx - most_significant_bit]
            
        return history