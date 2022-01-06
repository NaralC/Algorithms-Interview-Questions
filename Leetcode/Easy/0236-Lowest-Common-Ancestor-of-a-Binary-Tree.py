# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return dfs(root, p, q)
    
def dfs(root, p, q):
    #Time: O(n) worst case is where every node is explored
    #Space: O(n)
    #Run a waterfall-like searching algorithm - at each node return whether any targets are found
    
    #Case1: found nothing
    if not root: return None
    
    #Case2: found targets
    if root in [p, q]: return root
    
    #Default - return whether we found anything
    left = dfs(root.left, p, q)
    right = dfs(root.right, p, q)
    
    #Found both - this is the LCA
    if left and right:
        return root
    #Found either - return whichever one we found
    else:
        if left: return left
        if right: return right
    