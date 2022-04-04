# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Time: O(n)
        # Space: O(1)
        
        prev, current = None, head
        
        while current:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        
        return prev