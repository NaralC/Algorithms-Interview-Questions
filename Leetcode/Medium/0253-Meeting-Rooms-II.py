class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        #Time: O(nlogn)
        #Space: O(n)
        
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])
        ptr1, ptr2 = 0, 0
        count, maxCount = 0, 0
        
        while ptr1 < len(start) and ptr2 < len(end):
            val1 = start[ptr1]
            val2 = end[ptr2]
            
            if val1 < val2:
                count += 1
                ptr1 += 1
                maxCount = max(maxCount, count)
            else:
                count -= 1
                ptr2 += 1
                
        return maxCount