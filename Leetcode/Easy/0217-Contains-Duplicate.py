class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return trackWithSet(nums)
    
def trackWithSet(nums):
    #Time: O(n)
    #Space: O(n)
    seen = set()
    
    for num in nums:
        if num in seen:
            return True
        
        seen.add(num)
    
    return False
        
def setDifference(nums):
    #Time: O(n)
    #Space: O(?)

    return not len(nums) == len(set(nums))