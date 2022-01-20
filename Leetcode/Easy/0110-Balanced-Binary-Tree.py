# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #Time: O(n)
        #Space: O(n)
        return dfs(root)[0]
    
def dfs(root):
    #Null nodes are balanced by nature, and have no height
    if not root:
        return [True, 0] #[Balanced?, Height]
    
    left = dfs(root.left)
    right = dfs(root.right)
    
    balance = abs(left[1] - right[1]) <= 1 and (left[0] and right[0])
    
    return [balance, 1 + max(left[1], right[1])]