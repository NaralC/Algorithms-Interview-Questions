# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #Time: O(n)
        #Space: O(n)
        if not root: return []
        
        output = []
        queue = [root]
        
        while len(queue):
            currentLevel = []
            
            #BFS sub-problem
            for idx in range(len(queue)):
                node = queue.pop(0)
                
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                    
                currentLevel.append(node.val)
                
            output.append(currentLevel)
        
        return output