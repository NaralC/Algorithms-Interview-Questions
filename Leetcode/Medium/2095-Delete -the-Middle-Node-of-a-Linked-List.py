# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Time: O(n)
        #Space: O(1)
        
        dummy = ListNode('dummy', head)
        
        previous, slow, fast = dummy, head, head
        
        while fast and fast.next:
            previous = previous.next
            slow = slow.next
            fast = fast.next.next
        
        if slow == fast:
            return dummy.next.next
        
        previous.next = slow.next
        
        return head