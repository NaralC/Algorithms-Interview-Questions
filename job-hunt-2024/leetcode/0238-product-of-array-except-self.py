class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Time: O(n)
        # Space: O(n)

        fromLeft, fromRight = [1] * len(nums), [1] * len(nums)
        fromLeft[0] = nums[0]
        fromRight[-1] = nums[-1]

        # [1, 2, 6, 24]
        # [24, 24, 12, 4]

        for idx in range(1, len(nums)):
            fromLeft[idx] = nums[idx] * fromLeft[idx - 1]

        for idx in range(len(nums) - 2, -1, -1):
            fromRight[idx] = nums[idx] * fromRight[idx + 1]

        # Ship
        output = []

        for idx in range(len(nums)):
            left = fromLeft[idx - 1] if idx > 0 else 1
            right = fromRight[idx + 1] if idx < len(nums) - 1 else 1
            output.append(left * right)

        return output
        