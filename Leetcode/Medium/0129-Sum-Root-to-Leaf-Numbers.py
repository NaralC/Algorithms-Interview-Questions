# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        #Time: O(n) as we're visiting all nodes
        #Space: O(n)
        
        traverse(root, 0, output := [0])
        return output[0]
        
def traverse(root, current, output):
    if not root:
        return 0
    
    if root and not root.left and not root.right:
        current = (current * 10) + root.val
        output[0] += current
        return

    current = (current * 10) + root.val
    
    left = traverse(root.left, current, output)
    right = traverse(root.right, current, output)