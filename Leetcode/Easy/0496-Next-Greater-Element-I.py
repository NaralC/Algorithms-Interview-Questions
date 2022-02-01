class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #Time: O(n + m) where n = len(nums1), m = len(nums2)
        #Space: O(n)
        
        nextGreater = {} #{val : bigger_val}
        stack = [] #monotonic [big -> small]
        
        #Get the info of which number is smaller than which
        for num in nums2:
            while len(stack) and stack[-1] < num:
                nextGreater[stack.pop()] = num
            
            stack.append(num)
            
        #Map the info onto nums1 and return it
        for idx, num in enumerate(nums1):
            nums1[idx] = nextGreater.get(num, -1)
                
        return nums1