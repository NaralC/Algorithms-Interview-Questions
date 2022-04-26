# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Time: O(n)
        # Space: O(1)
        
        dummy = ListNode()
        ptr = dummy
        l1, l2 = list1, list2
        
        while l1 or l2:
            val1 = l1.val if l1 else float('inf')
            val2 = l2.val if l2 else float('inf')
        
            # Smaller value goes first
            if val1 < val2:
                ptr.next = l1
                l1 = l1.next
            else:
                ptr.next = l2
                l2 = l2.next
                
            ptr = ptr.next
        
        return dummy.next