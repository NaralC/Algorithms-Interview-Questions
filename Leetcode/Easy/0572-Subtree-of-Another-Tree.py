# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Time: O(n^2)
        # Space: O(n)
        # Perform a similarity check on every node
        if not root:
            return False
        
        if found(root, subRoot):
            return True
        
        # Only have to find a match once to verify
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
def found(root, subRoot):
    # Case 1: Both nodes are null
    if not root and not subRoot:
        return True
    
    # Case 2: Either node is null
    if not root or not subRoot:
        return False
    
    # Case 3: Both nodes are occupied, but have unmatching value
    if root.val != subRoot.val:
        return False
    
    # All nodes have to be strictly the same to validate as the same tree
    return found(root.left, subRoot.left) and found(root.right, subRoot.right)