# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #Time: O(n)
        #Space: O(1)
        
        #Setup variables
        dummy = ListNode('dummy', head)
        left, prevLeft = head, dummy
        right, prevRight = head, dummy
        temp = head
        
        #Get the pointers in place
        for _ in range(k - 1):
            left, prevLeft = left.next, prevLeft.next
        
        for _ in range(k):
            temp = temp.next
        
        while temp:
            right, prevRight = right.next, prevRight.next
            temp = temp.next
            
        #Begin the swapping process
        prevLeft.next = right
        prevRight.next = left
        right.next, left.next = left.next, right.next
    
        return dummy.next