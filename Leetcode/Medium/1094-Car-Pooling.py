class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        #Time: O(nlogn)
        #Space: O(n)
        
        #Contain (start/end points, passengers to pick up/drop off)
        timestamps = []
        
        for arr in trips:
            timestamps.append((arr[1], arr[0]))
            timestamps.append((arr[2], -arr[0]))
                
        #Loop through the time stamps in order
        count = 0 #tracks how passengers we're currently holding
        
        for stop, change in sorted(timestamps):
            count += change
            
            if count > capacity:
                return False
        
        return True