# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #Time: O(n) where w = max width of any level
        #Space: O(w)
        #Iterate through each level with its width, and only append the last nodes of each level to the output array
        
        output, q = [], collections.deque([root])
        
        while q:
            width = len(q)
            
            for idx in range(width):
                node = q.popleft()
                
                if node:
                    if idx + 1 == width:
                        output.append(node.val)
                    
                    if node.left: q.append(node.left)
                    if node.right: q.append(node.right)
                        
        return output