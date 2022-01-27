# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #Time: O(n)
        #Space: O(1)
        
        #It is best if we draw up the visualization while coding this up
        dummy = ListNode('dummy', head)
        
        #Phash 1 - put the ptr at position "left"
        previous = dummy
        current = head
        
        for idx in range(left - 1):
            previous = current
            current = current.next
            
        #Phase 2 - reverse the part "left" to "right"
        newHead = previous
        previous = None
        
        for idx in range(right - left + 1):
            nextNode = current.next
            current.next = previous
            previous = current
            current = nextNode
            
        #Phase 3 - clean up
        newHead.next.next = current
        newHead.next = previous
        
        return dummy.next
        