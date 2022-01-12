# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #Time: O(logn) since we're performing a binary search
        #Space: O(logn)
        
        def insert(currentNode):
            #Case1: val is on the left
            if val < currentNode.val:
                if not currentNode.left: 
                    currentNode.left = TreeNode(val)
                else:
                    insert(currentNode.left)
            
            #Case2: val is on the right
            else:
                if not currentNode.right:
                    currentNode.right = TreeNode(val)
                else:
                    insert(currentNode.right)
            
            #Return the root node
            return currentNode
        
        #Edge cases where there is no tree to start with
        if not root:
            return TreeNode(val)
        
        return insert(root)