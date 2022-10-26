class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # Time: O(sqrt(n))
        # Space: O(1)
        
        count = 0
        sqrt_n = int(pow(n, 0.5))
        
        for num in range(1, sqrt_n + 1):
            if n % num == 0: count += 1
            if count == k: return num
        
        for num in range(sqrt_n, 0, -1):
            if num * num == n: continue
                
            if n % num == 0: count += 1
            if count == k: return n // num
        
        return -1
    