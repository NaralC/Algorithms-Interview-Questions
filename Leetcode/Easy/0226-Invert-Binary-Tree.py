from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return bfs(root)

def bfs(root):
    # Time: O(n)
    # Space: O(w)
    if not root:
        return
    
    q = deque([root])
    
    while q:
        width = len(q)
        
        # Go level by level
        for _ in range(width):
            current = q.popleft()
            current.left, current.right = current.right, current.left # Swap the children
            
            if current.left: q.append(current.left) # Continue BFS
            if current.right: q.append(current.right)
    
    return root
    
def dfs(root):
    # Time: O(n)
    # Space: O(h)
    if not root:
        return
    
    root.left, root.right = root.right, root.left # Swap the children
    dfs(root.left) # Continue DFS
    dfs(root.right)
    
    return root