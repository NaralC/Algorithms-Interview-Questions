# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Time: O(n)
        # Space: O(1)
        # Floyd's Cycle Detection
        
        if not head: return
        
        # Detect if there's a loop
        slow, fast = head, head
        loop = False
        
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                loop = True
                break
        
        # No loop
        if not loop:
            return
        
        # Move the head ptr forward til it meets the slow ptr
        while head != slow:
            head = head.next
            slow = slow.next
        
        return head