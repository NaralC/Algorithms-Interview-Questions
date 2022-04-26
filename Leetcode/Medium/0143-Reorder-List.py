# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Time: O(n)
        # Space: O(1)
        
        # Find the middle of the list
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Divide the list into halves and reverse them
        prev = None
        
        while slow:
            nextNode = slow.next
            slow.next = prev
            prev = slow
            slow = nextNode
        
        # Merge the two halves into a new list
        dummy = ListNode()
        ptr = dummy
        l1, l2 = head, prev
        
        while l1 and l2:
            # Check for the middle element
            if l1 == l2:
                ptr.next = l1
                break
            
            # Left-right repeat
            ptr.next = l1
            ptr = ptr.next
            l1 = l1.next
            
            ptr.next = l2
            ptr = ptr.next
            l2 = l2.next
        
        return dummy.next
            