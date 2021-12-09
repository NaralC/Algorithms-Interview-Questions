# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #Time: O(n) where n = number of nodes in the tree
        #Space: O(n)
        travel = inorderTraverse(root, []) #inorder works since we're working with a BST
        return travel[k - 1] #1st smallest val -> val at idx 0
        
def inorderTraverse(root, history):
    if root == None:
        return history
    
    inorderTraverse(root.left, history)
    history.append(root.val)
    inorderTraverse(root.right, history)
    
    return history