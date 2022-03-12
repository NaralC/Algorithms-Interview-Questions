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
        #Space: O(n) due to the array holding all values
        
        def divide(start, end):
            if start > end:
                return
            
            mid = (start + end) // 2
            currentNode = TreeNode(nums[mid])
            currentNode.left = divide(start, mid - 1)
            currentNode.right = divide(mid + 1, end)
            
            return currentNode
        
        #Get node values into an array
        nums = []
        
        while head:
            nums.append(head.val)
            head = head.next
        
        #Recursively convert the numbers into a BST
        return divide(0, len(nums) - 1)