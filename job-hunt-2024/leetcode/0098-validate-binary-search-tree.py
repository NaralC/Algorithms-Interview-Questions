# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        # Time: O(n)
        # Space: O(n)

        vals = []

        def inorder(node):
            if not node: return
            inorder(node.left)
            vals.append(node.val)
            inorder(node.right)

        inorder(root)

        for idx in range(len(vals) - 1):
            cur, nxt = vals[idx], vals[idx + 1]

            if cur >= nxt: return False

        return True

    def DFS(self, root, minVal = float('-inf'), maxVal = float('inf')):
        # Time: O(n)
        # Space: O(h)
        # Visualizing this helps a ton! q 

        if not root: return True
        
        if not minVal < root.val < maxVal: return False
            
        # Cannot compare just immediate parents with children, needs to be the branch downwards
        return self.DFS(root.left, minVal, root.val) and self.DFS(root.right, root.val, maxVal)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        return self.DFS(root)
        # return self.inorderTraversal(root)