class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        #Time: O(nlogn)
        #Space: O(n)
        #Retrieve k largest numbers sorted by their idx
        
        nums = [(num, idx) for idx, num in enumerate(nums)]
        
        #Sort by value
        nums.sort(reverse = True)
        
        #Only take k biggest elements, and return them sorted by idx
        nums = sorted(nums[:k], key = lambda x: x[1])
        return [num for num, idx in nums]
    
        #Note - heap isn't rly needed since we're gonna to sort the array by their idx before returning anyways