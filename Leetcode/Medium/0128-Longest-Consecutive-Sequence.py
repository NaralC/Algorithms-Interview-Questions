class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        return hashSet(nums)
        
def hashSet(nums):
    # Time: O(n)
    # Space: O(n)
    if not len(nums): return 0

    seen = set(nums)
    output = 1

    # TLE optimization: iterate thru set to skip dupe numbers
    for num in seen:
        # TLE optimization: only look at starts of sequences, not ones in the middle
        if num - 1 in seen: continue

        length = 1
        curNum = num

        while curNum + 1 in seen:
            length += 1
            curNum += 1

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
