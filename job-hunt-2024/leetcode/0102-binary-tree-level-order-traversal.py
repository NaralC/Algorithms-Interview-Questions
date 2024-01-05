# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Time: O(n)
        # Space: O(n)

        q = deque([root])
        output = []

        while len(q):
            width = len(q)
            lvl = []

            for _ in range(width):
                node = q.popleft()
                if not node: continue

                q.append(node.left)
                q.append(node.right)

                lvl.append(node.val)

            output.append(lvl)

        return output[:-1]