# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        #Time: O(n)
        #Space: O(n)
        
        dfs(root, output := [], '')
        return output
    
def dfs(root, output, current):
    if not root: return
    
    if root and not root.left and not root.right:
        current += str(root.val)
        output.append(current)
        
    current += str(root.val) + '->'
    dfs(root.left, output, current)
    dfs(root.right, output, current)