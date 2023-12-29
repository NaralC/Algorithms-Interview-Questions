# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Time: O(n)
        # Space: O(n)

        seen = set()
        
        while head != None:
            # Check for dupes
            if head in seen: return True
            seen.add(head)

            # Move on
            head = head.next

        return False
        

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Time: O(n)
        # Space: O(1)

        if head == None or head.next == None: return False

        slow, fast = head, head.next

        # Floyd's cycle detection algo
        while fast and fast.next and fast.next.next:
            if slow == fast: return True

            slow = slow.next
            fast = fast.next.next

        return False
