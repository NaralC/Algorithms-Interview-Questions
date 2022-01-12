# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #Time: O(logn) since we're performing a binary search
        #Space: O(1)
        
        currentNode = root
        
        while currentNode:
            #Case1: target is on the right
            if val > currentNode.val:
                currentNode = currentNode.right
            
            #Case2: target is on the left
            elif val < currentNode.val:
                currentNode = currentNode.left
            
            #Case3: found the target
            else:
                return currentNode
        
        return None