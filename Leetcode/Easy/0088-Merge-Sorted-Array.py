class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #Time: O(n)
        #Space: O(1)
        one = len(nums1) - len(nums2) - 1
        two = len(nums2) - 1
        last = len(nums1) - 1

        while one > -1 and two > -1:
            if nums1[one] > nums2[two]:
                nums1[last] = nums1[one]
                one -= 1
            else:
                nums1[last] = nums2[two]
                two -= 1
            last -= 1
        
        #If there's a leftover in nums2
        while two > -1:
            nums1[last] = nums2[two]
            two -= 1
            last -= 1