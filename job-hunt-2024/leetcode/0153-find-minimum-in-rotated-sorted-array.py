class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Time: O(logn)
        # Space: O(1)

        # Arrays of length 1 or ascending arrays
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]

        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]

            if nums[lo] > nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1

        return -1
