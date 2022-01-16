class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #Time: O(2^n * n) (2^n) because it's a powerset; (*n) since we're looping over again and again
        #Space: O(2^n)
        
        allSubsets = [[]]
        
        for current in nums:
            #Iterate and fill data into a snapshot of allSubsets
            for idx in range(len(allSubsets)):
                allSubsets.append(allSubsets[idx] + [current])
        
        return allSubsets
        
        #    👇
        #[1,2,3]
        #allSubsets = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]