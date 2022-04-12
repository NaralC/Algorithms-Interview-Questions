class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        return hashSet(nums)
        
def hashSet(nums):
    # Time: O(n)
    # Space: O(n)

    output = 0
    lookup = set(nums)

    # Check for the longest sequence starting from every number
    for num in nums:
        # A number qualifies as a start if a number smaller than it by 1 doesn't exist
        if num - 1 not in lookup:
            length = 1

            while num + length in lookup:
                length += 1

            output = max(output, length)

    return output
        
def sorting(nums):
    # Time: O(nlogn)
    # Space: O(1)
    if not len(nums): return 0

    output = 0
    runningLength = 1
    nums.sort()

    for idx in range(len(nums) - 1):
        left, right = nums[idx], nums[idx + 1]

        if left == right:
            continue

        if left + 1 == right:
            runningLength += 1
        else:
            output = max(output, runningLength)
            runningLength = 1

    return max(output, runningLength)