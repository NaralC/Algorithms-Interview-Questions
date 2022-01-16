# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Time: O(n)
        #Space: O(1)
        
        left, right = None, head
        
        while right:
            nextNode = right.next
            right.next = left
            left = right
            right = nextNode
            
        return left