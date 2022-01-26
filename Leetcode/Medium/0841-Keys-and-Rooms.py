class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        #Time: O(m + n) where m = len(rooms), n = number of keys in each room
        #Space: O(m)
        
        #We start at room 0
        leftToVisit = [0]
        visited = {0}
        
        while len(leftToVisit):
            #Get the keys in form of indices
            newKeys = rooms[leftToVisit.pop()]
            
            for key in newKeys:
                if key not in visited:
                    visited.add(key) #Prevent repetitive work
                    leftToVisit.append(key) #Add new indices to visit later
        
        return len(visited) == len(rooms)