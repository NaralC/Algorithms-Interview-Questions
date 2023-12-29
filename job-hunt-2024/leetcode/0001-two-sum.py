class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time: O(nlogn)
        # Space: O(n)

        nums.sort()
        l, r = 0, len(nums) - 1

        while l != r:
            curVal = nums[l] + nums[r]

            if curVal == target: return [l, r]
            elif curVal > target: r -=1
            else: l += 1

        return False