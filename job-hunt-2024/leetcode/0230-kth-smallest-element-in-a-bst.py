# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Time: O(n)
        # Space: O(n)
        
        vals = []

        def inorder(root):
            if not root: return
            inorder(root.left)
            vals.append(root.val)
            inorder(root.right)
        
        inorder(root)

        return vals[k - 1]
