class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #Time: O(n)
        #Space: O(n)
        
        track = {} #[number, idx]
        
        for idx, num in enumerate(nums):
            if num in track.keys() and idx - track[num] <= k:
                return True
            
            track[num] = idx
        
        return False