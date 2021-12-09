# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #Time: O(n)
        #Space: O(n)
        return depthFirstSearch(root, [p, q])
    
def depthFirstSearch(root, target):
    #Base case: return whether we have found any targets or not
    if root == None or root in target:
        return root
    
    leftInfo = depthFirstSearch(root.left, target)
    rightInfo = depthFirstSearch(root.right, target)
    
    #Return this node as the LCA if we've found both targets under it
    if leftInfo and rightInfo:
        return root
    #Return one of the subtree that's not null
    else:
        return leftInfo if leftInfo else rightInfo