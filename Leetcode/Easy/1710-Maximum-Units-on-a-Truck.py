class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        #Time: O(nlogn)
        #Space: O(1)
        #Sort boxTypes by their units in descending order -> greedily dump boxes with higher units into the truck first
        output = 0
        boxTypes = sorted(boxTypes, key = lambda x: x[1], reverse = True)
        
        for numBox, units in boxTypes:
            #If we can dump all boxes down
            if truckSize > numBox:
                truckSize -= numBox
                output += numBox * units
                
            #If we can only dump some boxes
            else:
                output += truckSize * units
                break
        
        return output