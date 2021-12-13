class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ##Time: O(n)
        #Space: O(1)
        #Floyd's Cycle Detection Algorithm
        
        #Perform a slow-fast pointer loop check as usual
        slow, fast = 0, 0
        
        while True:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
            
            if fast == slow:
                break
        
        #Increment the head pointer until it meets the slow one
        head = 0
        while True:
            if slow == head:
                return slow
            
            slow = nums[slow]
            head = nums[head]