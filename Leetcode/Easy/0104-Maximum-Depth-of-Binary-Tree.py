from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return bfs(root)    
    
def dfs(root, count):
    # Time: O(n)
    # Space: O(h)
    if not root:
        return count
    
    count += 1
    return max(dfs(root.left, count), dfs(root.right, count))

def bfs(root):
    # Time: O(n)
    # Space: O(w)
    if not root: return 0

    q = deque([root])
    count = 0

    while q:
        width = len(q)
        count += 1 # Increments every time we encounter a new level

        for _ in range(width):
            current = q.popleft()

            if current.left: q.append(current.left)
            if current.right: q.append(current.right)

    return count