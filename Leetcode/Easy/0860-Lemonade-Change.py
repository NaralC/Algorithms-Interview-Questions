class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        #Time: O(n)
        #Space: O(1)
        
        cash = {5:0, 10:0, 20:0} #{bill : number of bills}
        
        for bill in bills:
            #Update our variables
            cash[bill] += 1
                        
            #Allocate bills for the change
            change = bill - 5
            
            if change == 15: #5 x 3, 5 x 1 + 10 x 1
                if cash[10] >= 1 and cash[5] >= 1:
                    cash[10] -= 1
                    cash[5] -= 1
                    
                elif cash[5] >= 3:
                    cash[5] -= 3
                
                else:
                    return False
                
            elif change == 5: #5 x 1
                if cash[5] >= 1:
                    cash[5] -= 1
                
                else:
                    return False
            
        return True