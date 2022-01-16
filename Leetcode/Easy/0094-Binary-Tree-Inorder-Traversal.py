# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #Time: O(n)
        #Space: O(n)   
    
        def traverse(root):
            if not root:
                return
            
            traverse(root.left)
            output.append(root.val)
            traverse(root.right)
            
        output = []
        traverse(root)
        
        return output