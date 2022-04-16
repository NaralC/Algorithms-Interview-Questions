# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Time: O(n)
        # Space: O(n)
        
        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            # Update the diameter := max(diameter, leftDepth + rightDepth)
            diameter[0] = max(diameter[0], left + right)
            
            # The diameter only counts a single path from each side
            return 1 + max(left, right)
        
        diameter = [0]
        dfs(root)
        return diameter[0]