# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Time: O(min(p, q))
        # Space: O(min(p, q))

        if p == None and q == None: return True # Both null
        if p == None or q == None: return False # Either is null

        leftTruthVal = self.isSameTree(p.left, q.left)
        rightTruthVal = self.isSameTree(p.right, q.right)

        return leftTruthVal and rightTruthVal and p.val == q.val