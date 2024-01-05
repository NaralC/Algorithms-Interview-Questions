# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Time: O(n)
        # Space: O(1)

        # Count how many nodes there are
        count = 0
        ptr = head

        while ptr:
            count += 1
            ptr = ptr.next
        
        # Traverse to the nth node (counting from the back)
        dummy = ListNode(0, head)
        prev, cur = dummy, head

        for _ in range(count - n):
            prev = prev.next
            cur = cur.next

        # Delete the node in question
        prev.next = cur.next
        cur.next = None

        return dummy.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Time: O(n)
        # Space: O(1)
        
        # Traverse to the nth node (counting from the back)
        slow, fast = head, head
        
        # Fast and slow should be n nodes apart
        # This is a one-pass substitute to counting the nodes
        for _ in range(n):
            fast = fast.next

        # Case where we delete the first node
        if not fast: return slow.next

        # Move fast to the end of list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        # Remove the node in question
        slow.next = slow.next.next
        return head