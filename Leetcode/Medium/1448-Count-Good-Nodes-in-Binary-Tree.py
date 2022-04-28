# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Time: O(n)
        # Space: O(d)
        
        def dfs(node, maxVal):
            if not node:
                return
            
            if node.val >= maxVal:
                count[0] += 1
                maxVal = max(maxVal, node.val)
            
            dfs(node.left, maxVal)
            dfs(node.right, maxVal)
            
        
        count = [0] # The root is always good
        dfs(root, root.val)
        return count[0]