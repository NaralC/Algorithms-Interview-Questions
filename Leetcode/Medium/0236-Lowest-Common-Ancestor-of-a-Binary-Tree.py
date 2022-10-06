# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Time: O(h)
        # Space: O(h)
        
        # Assuming:
        # No null/empty inputs are allowed
        # No duplicate nodes allowed
        # The number of nodes fit in memory
        # The tree is always binary
        
        # Solution:
        def dfs(node):
            if not node:
                return
            
            if node in [p, q]:
                return node
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if left and right:
                return node
            return left or right
        
        return dfs(root)
    