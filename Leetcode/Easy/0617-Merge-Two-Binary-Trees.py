# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        return mergeNodes(root1, root2)

def mergeNodes(root1, root2):
    #Time: O(m + n) where m = number of nodes in root1, n = number of nodes in root2
    #Space: O(m + n)
    if not root1 and not root2:
        return None
    
    root1_val = root1.val if root1 else 0
    root2_val = root2.val if root2 else 0
    newNode = TreeNode(root1_val + root2_val)

    newNode.left = mergeNodes(root1.left if root1 else None, root2.left if root2 else None)
    newNode.right = mergeNodes(root1.right if root1 else None, root2.right if root2 else None)

    return newNode