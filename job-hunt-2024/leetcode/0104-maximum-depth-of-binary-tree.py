# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Time: O(n)
        # Space: O(h) or O(w)

        if root == None: return 0

        def bfs(node):
            q = deque()
            q.append(node)
            depth = -1

            while len(q) > 0:
                qLen = len(q)

                for _ in range(qLen):
                    curNode = q.popleft()
                    if curNode == None: continue

                    q.append(curNode.left)
                    q.append(curNode.right)

                depth += 1

            return depth

        def dfs(node, curDepth):
            if node == None: return curDepth

            leftDepth = dfs(node.left, curDepth + 1)
            rightDepth = dfs(node.right, curDepth + 1)
            return max(leftDepth, rightDepth)

        return bfs(root)