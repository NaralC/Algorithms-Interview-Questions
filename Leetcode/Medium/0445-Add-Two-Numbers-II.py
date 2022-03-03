# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #Time: O(max(l1, l2))
        #Space: O(max(l1, l2))
        
        #Reverse both lists to start from their least significant bits
        l1 = reverseList(l1)
        l2 = reverseList(l2)
        
        #Start the adding process
        carry = 0
        newHead = ListNode('dummy')
        ptr = newHead
        
        while l1 or l2 or carry:
            carry += l1.val if l1 else 0
            carry += l2.val if l2 else 0
            
            newNode = ListNode(carry % 10)
            ptr.next = newNode
            ptr = newNode
            carry //= 10
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        #Reverse the list back to its normal form
        return reverseList(newHead.next)
        
def reverseList(head):
    prev = None
    
    while head:
        nextNode = head.next
        head.next = prev
        prev = head
        head = nextNode
        
    return prev