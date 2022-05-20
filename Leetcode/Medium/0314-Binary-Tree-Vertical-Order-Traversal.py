from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Time: O(nlogn)
        # Space: O(n)
        
        if not root: return []
        
        # Simply put: return node vals which share the same x coordinate
        coordinates = defaultdict(list)
        q = deque([(root, 0)])
        
        while len(q):
            node, x = q.popleft()
            
            # Map coordinates to each node
            coordinates[x].append(node.val)
            
            if node.left: q.append((node.left, x - 1))
            if node.right: q.append((node.right, x  + 1))
            
        return [vals for x, vals in sorted(coordinates.items())]