class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return mooreAlgo(nums)
        
def mooreAlgo(nums):
    #Time: O(n)
    #Space: O(1)
    
    curNum, count = nums[0], 1
    
    for num in nums[1:]:
        if count == 0:
            curNum, count = num, 1
            continue
        
        if num == curNum:
            count += 1
        else:
            count -= 1
            
    return curNum

def hashTable(nums):
    #Time: O(n)
    #Space: O(n)
    
    track = {} #[number, frequency]

    for num in nums:
        track[num] = track.get(num, 0) + 1

    highestNum, highestFreq = 0, 0
    for num, freq in track.items():
        if freq > highestFreq:
            highestFreq = freq
            highestNum = num

    return highestNum