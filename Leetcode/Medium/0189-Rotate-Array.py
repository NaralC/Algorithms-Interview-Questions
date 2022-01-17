class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        straightforward(nums, k)
        
def straightforward(nums, k):
    #Time: O(n)
    #Space: O(n)
    
    #Allocate an array for storing rotated elements
    rotated = [None for _ in range(len(nums))]
    
    #Rotate the numbers given
    for idx, num in enumerate(nums):
        newIdx = (idx + k) % len(nums)
        rotated[newIdx] = num
    
    #Assign the rotated numbers back to the input array
    for idx, num in enumerate(rotated):
        nums[idx] = rotated[idx]
 
def optimized(nums, k):
    #Time: O(n)
    #Space: O(1)
    
    #k = rotate k elements counting from the back
    #nums = [1, 2, 3, 4 | 5, 6, 7] while k = 3
    #nums[::-1] = [7, 6, 5 | 4, 3, 2, 1]
    
    #Reverse left & right separately where:
    #left = nums[:k], right = nums[k:]
    
    #Prevent idx out of bound
    k %= len(nums)

    #Reverse the entire array first
    reverseArray(0, len(nums) - 1, nums)

    #Reverse the two arrays diveded like this: nums[:k], nums[k:]
    reverseArray(0, k - 1, nums) #Reverse the left half
    reverseArray(k, len(nums) - 1, nums) #Reverse the right half

        
def reverseArray(left, right, nums):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left, right = left + 1, right - 1