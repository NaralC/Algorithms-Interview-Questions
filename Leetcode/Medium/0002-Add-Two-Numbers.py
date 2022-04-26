# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Time: O(n)
        # Space: O(n)
        
        dummy = ListNode()
        ptr = dummy
        carry = 0
        
        while carry or l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
            
            if l2:
                carry += l2.val
                l2 = l2.next
            
            newNode = ListNode(carry % 10)
            carry //= 10
            ptr.next = newNode
            ptr = ptr.next
            
        return dummy.next