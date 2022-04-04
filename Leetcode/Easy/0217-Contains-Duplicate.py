class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return utilizeSet(nums)
        
def utilizeSet(nums):
    # Time: O(n)
    # Space: O(n)

    seen = dict()

    for num in nums:
        if num in seen:
            return True
        seen[num] = True

    return False
        
def sorting(nums):
    # Time: O(nlogn)
    # Space: O(1)

    nums.sort()

    for idx in range(1, len(nums)):
        left, right = nums[idx - 1], nums[idx]

        if left == right:
            return True

    return False