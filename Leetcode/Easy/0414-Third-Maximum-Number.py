class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        #Time: O(n)
        #Space: O(1)
        
        output = [float('-inf')] * 3 #small -> large
        
        for num in nums:
            #Prevent dealing with duplicates
            if num in output:
                continue
            
            if num > output[0]:
                if num > output[1]:
                    if num > output[2]:
                        output[0] = output[1] #Shift the answers to the left to make room
                        output[1] = output[2]
                        output[2] = num
                    
                    else:
                        output[0] = output[1] #Shift the answers to the left to make room
                        output[1] = num
                
                else:
                    output[0] = num
        
        return output[0] if output[0] != float('-inf') else output[2]