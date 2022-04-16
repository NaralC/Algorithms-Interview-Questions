# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Time: O(n)
        # Space: O(n)
        
        def dfs(root):
            # Null nodes are have no height, and are considered balanced
            if not root:
                return [0, True] # [Height, Balance]
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            # Check the current's node balance (height diff & bottom-up inherited balance)
            balance = abs(left[0] - right[0]) <= 1 and (left[1] and right[1])
        
            return [1 + max(left[0], right[0]), balance]
            
        return dfs(root)[1]