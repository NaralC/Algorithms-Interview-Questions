# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Time: O(n)
        #Space: O(1)
        
        #Setup variables
        dummy = ListNode('dummy', head)
        current = dummy
        
        #Keep swapping pairs if there's another pair ahead
        while current.next and current.next.next:
            left, right = current.next, current.next.next
            nextNode = right.next
            
            #Swap
            current.next = right
            right.next = left
            left.next = nextNode
            
            #Proceed
            current = current.next.next
            
        return dummy.next