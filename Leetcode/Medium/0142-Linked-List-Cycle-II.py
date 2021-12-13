# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Time: O(n)
        #Space: O(1)
        #Floyd's Cycle Detection Algorithm
        
        #Perform a slow-fast pointer loop check as usual
        slow, fast = head, head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                break
        
        #Determine whether we're out of bound
        if not fast or not fast.next:
            return None
        
        #Increment the head pointer until it meets the slow one
        while head:
            if head == slow:
                return head
            
            head = head.next
            slow = slow.next