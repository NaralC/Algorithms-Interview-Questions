# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Time: O(n)
        # Space: O(w)

        q = deque()
        q.append(root)

        while len(q) > 0:
            qLen = len(q)

            for _ in range(qLen):
                current = q.popleft()
                if current == None: continue

                current.left, current.right = current.right, current.left
                q.append(current.left)
                q.append(current.right)

        return root


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Time: O(?)
        # Space: O(?)

        if root == None: return

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root