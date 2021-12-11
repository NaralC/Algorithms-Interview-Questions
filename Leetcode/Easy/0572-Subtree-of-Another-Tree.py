# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #Time: O(root * subRoot) #As we perform a mirror check on every node
        #Space: O(root * subRoot)
        if not root: return False #Since there's nothing to check
        if not subRoot: return True #Emptiness is a always a subtree
        
        if mirrorCheck(root, subRoot):
            return True
        
        leftInfo = self.isSubtree(root.left, subRoot)
        rightInfo = self.isSubtree(root.right, subRoot)
        
        #We only need one check to validate to confirm their similarity
        return leftInfo or rightInfo
    
def mirrorCheck(root1, root2):
    #Both are null
    if not root1 and not root2:
        return True
    
    #Either is null / Both are occupied, but with different values
    if (not root1 or not root2) or (root1.val != root2.val):
        return False
    
    return mirrorCheck(root1.left, root2.left) and mirrorCheck(root1.right, root2.right)