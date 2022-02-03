class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        #Time: O(n^2)
        #Space: O(n^2)
        
        #a + b + c + d = 0
        #a + b = -c -d
        #a + b = -(c + d)
        #If the condition above passes, that means we have a 4-element tuple that adds up to 0
        
        seen, count = dict(), 0
        
        for a in nums1:
            for b in nums2:
                seen[a + b] = seen.get(a + b, 0) + 1
                
        for c in nums3:
            for d in nums4:
                count += seen.get(-(c + d), 0)
                
        return count