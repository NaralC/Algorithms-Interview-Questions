class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #Time: O(n)
        #Space: O(1)
        slow = 1 #We're skipping 0-th idx since it's already unique
        for fast in range(1, len(nums)):
            #If fast runs into a new number
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1

        return slow