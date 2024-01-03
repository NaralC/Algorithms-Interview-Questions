class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Time: O(logn)
        # Space: O(1)

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            guess = nums[mid]

            if guess > target:
                high = mid - 1
            elif guess < target:
                low = mid + 1
            else:
                return mid

        return -1
