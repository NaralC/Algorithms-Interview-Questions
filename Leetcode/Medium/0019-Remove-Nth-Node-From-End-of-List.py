# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #Time: O(n)
        #Space: O(1)
        slow, fast = head, head
        
        #Fast and slow should be n nodes apart
        for _ in range(n):
            fast = fast.next
        
        #Edge case where we remove the first node
        if fast == None:
            return slow.next
        
        #Move fast to the end of list
        while fast.next != None:
            slow, fast = slow.next, fast.next
        
        #Delete the node next to slow (nth node from end)
        slow.next = slow.next.next
        return head