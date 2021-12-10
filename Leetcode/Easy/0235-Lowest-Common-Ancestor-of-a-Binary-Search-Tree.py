# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return binarySearch(root, [p, q])
    
def binarySearch(root, target):
    #Time: O(log(n)) as this is binary search's time complexity
    #Space: O(1)
    p, q = target[0], target[1]
    curNode = root
    
    while curNode:
        #Case 1: both targets are on the right
        if p.val > curNode.val and q.val > curNode.val:
            curNode = curNode.right
        #Case 2: both targets are on the left
        elif p.val < curNode.val and q.val < curNode.val:
            curNode = curNode.left
        #Case 3: targets split up; thus we return this node as the LCA
        else:
            return curNode
    
def depthFirstSearch(root, target):
    #Time: O(n)
    #Space: O(n)
    
    #Case 1: we don't find any targets
    if not root:
        return None
    
    #Case 2: we've found one of the targts
    if root in target:
        return root
    
    leftInfo = depthFirstSearch(root.left, target)
    rightInfo = depthFirstSearch(root.right, target)
    
    #Return this node as the LCA as we've found where the targets lead up to
    if leftInfo and rightInfo:
        return root
    #If not, we return a target we find in the process
    else:
        return leftInfo if leftInfo else rightInfo