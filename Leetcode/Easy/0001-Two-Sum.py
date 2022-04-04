class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time: O(n)
        # Space: O(n)
        
        seen = dict() #{val : idx}
        
        for idx, num in enumerate(nums):
            diff = target - num
            
            if diff in seen:
                return [seen[diff], idx]
            seen[num] = idx
        
        return