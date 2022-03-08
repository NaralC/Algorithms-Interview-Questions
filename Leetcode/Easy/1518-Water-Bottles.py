class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        #Time: O(n)
        #Space: O(1)
        
        full, empty, output = numBottles, 0, 0
        
        while full > 0:
            #Drink
            output += full
            empty += full
            full = 0
            
            #Exchange
            full += empty // numExchange
            empty %= numExchange
        
        return output