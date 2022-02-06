class Solution:
    def numberOfSteps(self, num: int) -> int:
        #Time: O(n)
        #Space: O(1)
        if not num: return 0
        
        count = 0
        
        while num > 0:
            #Encounter 0 -> divide (+1)
            #Encounter 1 -> substract and divide (+2)
            #Example: to shift 111 (7) one time to the right and get 11 (3), we need to substract 1 from it first then divide it by 2; hence the (+2)
            count += (num & 1) + 1
            
            num = num >> 1
            
        return count - 1