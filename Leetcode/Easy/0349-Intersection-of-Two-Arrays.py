class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return method2(nums1, nums2)
 
def method2(nums1, nums2):
    #Time: O(n + m)
    #Space: O(min(n, m))
    
    seen1, seen2 = set(), set()
    
    for num in nums1:
        seen1.add(num)
        
    for num in nums2:
        if num in seen1:
            seen2.add(num)
            seen1.remove(num)
    
    return seen2
        
def method1(nums1, nums2):
    #Time: O(nlogn + mlogm)
    #Space: O(min(n, m))

    nums1.sort()
    nums2.sort()

    ptr1, ptr2 = 0, 0
    intersection = set()

    while ptr1 < len(nums1) and ptr2 < len(nums2):
        #Case1: ptr1 < ptr2:
        if nums1[ptr1] < nums2[ptr2]:
            ptr1 += 1

        #Case2: ptr1 > ptr2:    
        elif nums1[ptr1] > nums2[ptr2]:
            ptr2 += 1

        #Case3: ptr1 == ptr2 (found an intersection)
        else:
            intersection.add(nums1[ptr1])
            ptr1 += 1
            ptr2 += 1

    return intersection