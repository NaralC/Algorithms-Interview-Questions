# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #Time: O(max(l1, l2))
        #Space: O(max(l1, l2))
        #Same idea as 'Add Binary'
        
        newList = ListNode('dummy')
        head = newList
        carry = 0
        
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
                
            newNode = ListNode(carry % 10)
            carry = carry // 10
            newList.next = newNode
            newList = newNode
            
        return head.next