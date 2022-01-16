# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Time: O(n)
        #Space: O(1)
        
        left, right = head, head
        
        #The two ptrs have to be n nodes apart
        for idx in range(n):
            right = right.next
        
        #Edge case: n = len(linked list)
        #Remove the first node
        if not right:
            return head.next
        
        #Loop until the right ptr lands on the end of list
        while right.next:
            left = left.next
            right = right.next
        
        #Make left ptr skip the node next to it
        left.next = left.next.next
        
        return head