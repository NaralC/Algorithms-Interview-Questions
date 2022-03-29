from heapq import heapify, heappop

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        #Time: O(nlogn)
        #Space: O(n)
        
        #Greedily connect the smallest sticks first using a min heap
        heapify(sticks)
        
        #Go through our stick pile
        cost = 0
        
        while len(sticks) >= 2:
            #Take out the 2 smallest sticks
            s1 = heappop(sticks)
            s2 = heappop(sticks)
            
            #Put it back into the heap as one (also increment cost)
            cost += s1 + s2
            heappush(sticks, s1 + s2)
        
        return cost