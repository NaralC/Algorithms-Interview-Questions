# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next  next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Time: O(n)
        # Space: O(n)
        
        # Reverse both lists
        l1 = reverseList(l1)
        l2 = reverseList(l2)
        
        # Add them up
        carry = 0
        newList = ListNode('dummy')
        head = newList
        
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
                
            newList.next = ListNode(carry % 10)
            newList = newList.next
            carry //= 10
            
        return reverseList(head.next)
        
def reverseList(l):
    prev = None

    while l:
        nxtNode = l.next
        l.next = prev
        prev = l
        l = nxtNode

    return prev
