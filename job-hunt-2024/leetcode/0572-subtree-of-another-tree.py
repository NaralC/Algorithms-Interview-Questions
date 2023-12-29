# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Time: O(rootSize * subRootSize)
        # Space: O(rootSize * subRootSize)

        def sameTree(a, b):
            if a == None and b == None: return True # Both null
            if a == None or b == None: return False # Either is null

            leftCheck = sameTree(a.left, b.left)
            rightCheck = sameTree(a.right, b.right)

            return leftCheck and rightCheck and a.val == b.val

        # Call the sameTree function on every node
        if subRoot == None: return True
        if root == None: return False
        if sameTree(root, subRoot): return True

        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right 