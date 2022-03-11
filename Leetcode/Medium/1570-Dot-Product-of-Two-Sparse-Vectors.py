class SparseVector:
    def __init__(self, nums: List[int]):
        self.idx_num = [(idx, num) for idx, num in enumerate(nums) if num > 0]
        
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        #Time: O(n)
        #Space: O(n)
        #Store indices and numbers into paris - then use use 2-ptr like merging sorted arrays/lists
        
        arr1, arr2 = self.idx_num, vec.idx_num
        ptr1, ptr2, output = 0, 0, 0
        
        while ptr1 < len(arr1) and ptr2 < len(arr2):
            idx1, idx2 = arr1[ptr1][0], arr2[ptr2][0]
            
            if idx1 < idx2:
                ptr1 += 1
            elif idx1 > idx2:
                ptr2 += 1
            else:
                output += arr1[ptr1][1] * arr2[ptr2][1]
                ptr1 += 1; ptr2 += 1
        
        return output

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)