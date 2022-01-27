# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        #Time: O(n)
        #Space: O(n)
        
        def dfs(root, currentSum, currentPath):
            if not root:
                return
            
            currentSum += root.val
            newPath = currentPath.copy() #Creat a new copy to avoid using references
            newPath.append(root.val)
            
            if root and not root.left and not root.right and currentSum == targetSum:
                output.append(newPath)
                
            dfs(root.left, currentSum, newPath)
            dfs(root.right, currentSum, newPath)
            
        output = []
        dfs(root, 0, [])
        return output