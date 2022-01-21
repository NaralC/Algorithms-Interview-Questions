class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        #Time: O(nlogn)
        #Space: O(n)
        
        #Greedy pairing:
        #min(large, large) = large output
        #min(large, small) = small output
        #So we prioritize pairing large values together
        #Essentially we can just add up nums at idx 0, 2, 4, ...
        
        nums.sort()
        return sum([nums[idx] for idx in range(0, len(nums), 2)])