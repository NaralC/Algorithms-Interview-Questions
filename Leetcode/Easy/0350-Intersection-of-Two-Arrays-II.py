class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return hashTable(nums1, nums2)
    
def hashTable(nums1, nums2):
    #Time: O(n + m)
    #Space: O(min(n, m)) counting the hashtable
    frequency = {}
    intersection = []
    
    for num in nums1:
        frequency[num] = frequency.get(num, 0) + 1
    
    for num in nums2:
        if frequency.get(num, 0) > 0:
            intersection.append(num)
            frequency[num] -= 1
    
    return intersection
    
def twoPointers(nums1, nums2):
    #Time: O(n*log(n) + m*log(m))
    #Space: O(1) if we disregard the output, O(min(n, m)) if we count it
    nums1.sort()
    nums2.sort()
    intersection = []
    
    one, two = 0, 0    
    while one < len(nums1) and two < len(nums2):
        valOne = nums1[one]
        valTwo = nums2[two]
        
        if valOne == valTwo:
            intersection.append(valOne)
            one += 1
            two += 1
        elif valOne > valTwo:
            two += 1
        else:
            one += 1
    
    return intersection