# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], target: int) -> Optional[ListNode]:
        #Time: O(n)
        #Space: O(1)
        
        current = ListNode('dummy', head)
        newHead = current
        
        while current:
            #Skip the next nodes if they match the target
            while current.next and current.next.val == target:
                current.next = current.next.next
            
            current = current.next
            
        return newHead.next