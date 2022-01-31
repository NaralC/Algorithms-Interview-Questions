class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Time: O(n)
        #Space: O(1)
        #Only one element can appear more than 1/2 of the time, think of it in fractions!
        
        count, current = 0, None
        
        for num in nums:
            #Character match
            if num == current:
                count += 1
            
            #Reset counter and current candidate
            elif count == 0:
                current, count = num, 1
            
            #Character mismatch
            else:
                count -= 1
            
        return current