class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Time: O(nlogn)
        # Space: O(n)
        
        # Sort the array, so the numbers are in ascending order
        # idx is for when we assign information back to output later on
        nums = sorted([(num, idx) for idx, num in enumerate(nums)]) 
        
        # Use a hash table to track the first appearance of each number
        firstSeen = dict()
        
        for idx in range(len(nums)):
            if nums[idx][0] in firstSeen:
                continue
            firstSeen[nums[idx][0]] = idx
        
        # Loop through nums, assign the idx of each number's first appearance to the output
        # This works since the array is sorted and we use the first appearance to deal with duplicates
        output = [0] * len(nums)
        
        for num, idx in nums:
            output[idx] = firstSeen[num]
        
        return output