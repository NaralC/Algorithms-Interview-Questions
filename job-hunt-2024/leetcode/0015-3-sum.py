class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Time: O(n^2)
        # Space: O(n)

        # Sort -> two pointers
        nums.sort()
        output = set()

        for idx in range(len(nums)):
            l, r = idx + 1, len(nums) - 1

            while l < r:
                curVal = nums[idx] + nums[l] + nums[r]

                if curVal > 0:
                    r -= 1
                elif curVal < 0:
                    l += 1
                else:
                    output.add((nums[idx], nums[l], nums[r]))
                    r -= 1
                    l += 1

        return list(output)
