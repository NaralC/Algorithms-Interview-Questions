from collections import defaultdict

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # Time: O(nlogn * n)
        # Space: O(n)
        
        lookup = defaultdict(list)
        
        for num in arr:
            lookup[bin(num).count('1')].append(num)
            
        output = []
        
        for count, nums in sorted(lookup.items()):
            for num in sorted(nums):
                output.append(num)
                
        return output
    