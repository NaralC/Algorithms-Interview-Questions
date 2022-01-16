class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Time: O(n)
        #Space: O(1)
        
        slow, fast = 0, 0
        
        while fast < len(nums):
            #Swap when: slow is on zero & fast is on non-zero
            if nums[slow] == 0 and nums[fast] != 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]
            
            #Increment slow until it finds a zero
            if nums[slow] != 0:
                slow += 1
                
            fast += 1