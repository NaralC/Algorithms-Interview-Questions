class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        # Time: O(nlogn + mlogm)
        # Space: O(1)
        
        # Find a pair of arrays that overlap the earliest (and still be in duration)
        idx1 = idx2 = 0
        slots1.sort()
        slots2.sort()
        
        while idx1 < len(slots1) and idx2 < len(slots2):
            # Overlap
            s1, e1 = slots1[idx1]
            s2, e2 = slots2[idx2]
            
            if e1 > s2:
                start = max(s1, s2)
                end = min(e1, e2)
                
                if end - start >= duration:
                    return [start, start + duration]
            
            # Move on from the one that ends first
            if e1 < e2:
                idx1 += 1
            else:
                idx2 += 1
        
        return []
    
    