class Solution:
    def average(self, salary: List[int]) -> float:
        #Time: O(n)
        #Space: O(1)
        
        low, high = float('inf'), float('-inf')
        total = 0
        
        for num in salary:
            low, high = min(low, num), max(high, num)
            total += num
        
        return (total - low - high) / (len(salary) - 2)