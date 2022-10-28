# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict, deque

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Time: O(n)
        # Space: O(n)
        
        # Map nodes to their corresponding cols
        q = deque([(root, 0)])
        lookup = defaultdict(list) # { col: [node1, node2, ...] }
        
        while len(q):
            node, col = q.popleft()
            lookup[col].append(node.val)
            
            if node.left: q.append((node.left, col - 1))
            if node.right: q.append((node.right, col + 1))
        
        # Ship output
        output = []
        
        for col, nodeList in sorted(lookup.items()):
            output.append(nodeList)
        
        return output
    