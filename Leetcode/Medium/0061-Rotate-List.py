# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #Time: O(n)
        #Space: O(1)
        
        #[1 -> 2 -> 3 -> 4 -> 5]
        #[1 -> 2 -> 3 -> NULL] and [4 -> 5 -> 1]
        #[5 -> 4 -> 3 -> 2 -> 1]
        
        if not head: return head
        
        #Make the last node point to the first node
        current = head
        length = 1
        
        while current.next:
            length += 1
            current = current.next
        
        current.next = head
        
        #Make the (length - k - 1)th node point to null, and return the node after it
        k %= length
        current = head
        
        for idx in range(length - k - 1):
            current = current.next
        
        newHead = current.next
        current.next = None
        
        return newHead
        