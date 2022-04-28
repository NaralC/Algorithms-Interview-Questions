from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Time: O(n)
        # Space: O(w)
        
        if not root: return []
        
        output = []
        q = deque([root])
        
        while len(q):
            width = len(q)
            lvl = []
            
            for idx in range(width):
                node = q.popleft()
                
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                
                lvl.append(node.val)
            
            output.append(lvl)
        
        return output[::-1]