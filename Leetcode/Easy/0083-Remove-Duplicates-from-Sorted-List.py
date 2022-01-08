# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Time: O(n)
        #Space: O(1)
        current = head
        
        while current:
            #Skip the next nodes if they have a duplicate value
            while current.next and current.next.val == current.val:
                current.next = current.next.next
            
            current = current.next
        
        return head