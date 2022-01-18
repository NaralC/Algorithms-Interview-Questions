# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        #Time: O(n)
        #Space: O(n)
        
        if not root: return 0
        
        dfs(root, output := [0], False)
        return output[0]
    
def dfs(root, output, isLeft):
    if not root:
        return
    
    if isLeft and not root.left and not root.right:
        output[0] += root.val
    
    dfs(root.left, output, True)
    dfs(root.right, output, False)