# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target: int) -> bool:
        return dfs(root, target, 0)
    
def dfs(root, target, curSum):
    #Time: O(n)
    #Space: O(n)
    #Note: root-to-leaf path means we must go all the way down, can't stop mid-way even if the curSum == target
    
    curSum += root.val if root else 0
    
    if not root:
        return False
    
    if curSum == target and (not root.left and not root.right):
        return True

    left = dfs(root.left, target, curSum)
    right = dfs(root.right, target, curSum)
    
    return left or right