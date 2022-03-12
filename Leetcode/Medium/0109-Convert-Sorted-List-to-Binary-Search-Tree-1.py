# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        #Time: O(n) since we visit every node
        #Space: O(logn) due to the recursive call stack of a BST
        
        #Find the list's length
        length = 0
        ptr = head
        
        while ptr:
            length += 1
            ptr = ptr.next
        
        def divide(start, end):
            if start > end:
                return
            
            #Allow global access of the variable
            nonlocal head
            
            #We utilize the nature of inorder traversal to traverse through a BST in ascending order
            mid = (start + end) // 2
            
            #Go left
            left = divide(start, mid - 1)
            
            #Take action in the middle
            currentNode = TreeNode(head.val)
            currentNode.left = left
            head = head.next
            
            #Go right
            currentNode.right = divide(mid + 1, end)
            
            return currentNode
        
        return divide(0, length - 1)