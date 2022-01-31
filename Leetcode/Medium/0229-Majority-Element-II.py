class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        return boyerAlgo(nums)
    
def boyerAlgo(nums):
    #Time: O(n)
    #Space: O(1)
    #Only two elements can appear 1/3 times, think of it in terms of fraction!
    
    count1, candidate1 = 0, None
    count2, candidate2 = 0, None
    
    for num in nums:
        #Character match
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
            
        #Reset count and candidate
        elif count1 == 0:
            count1, candidate1 = 1, num
        elif count2 == 0:
            count2, candidate2 = 1, num
            
        #Character mismatch
        else:
            count1 -= 1
            count2 -= 1
    
    return [c for c in [candidate1, candidate2] if nums.count(c) > (len(nums) // 3)]
    
def hashTable(nums):
    #Time: O(n)
    #Space: O(n)

    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1 #{num : frequency}

    output = []
    for key, value in freq.items():
        if value > (len(nums) // 3):
            output.append(key)

    return output