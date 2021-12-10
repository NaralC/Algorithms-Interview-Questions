# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #Time: O(p + q)
        #Space: O(n)
        return depthFirstSearch(p, q)

def depthFirstSearch(p, q):
    #Case 1: both nodes are null
    if not p and not q:
        return True
    
    #Case 2: (One of the nodes is null) or (Both are occupied, but their values don't match)
    if (not p or not q) or (p.val != q.val):
        return False
    
    leftInfo = depthFirstSearch(p.left, q.left)
    rightInfo = depthFirstSearch(p.right, q.right)
    
    return leftInfo and rightInfo
    