# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Time: O(n)
        # Space: O(n)
        
        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            nums.append(root.val)
            inorder(root.right)
            
        # With inorder's nature, the values must strictly be in ascending order
        nums = []
        inorder(root)
        
        for idx in range(1, len(nums)):
            prev, cur = nums[idx - 1], nums[idx]
            
            if prev >= cur:
                return False
        
        return True