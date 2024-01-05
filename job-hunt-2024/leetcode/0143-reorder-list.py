# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Time: O(n)
        # Space: O(n)
        
        # Keep the data in a different DS
        nums = deque()
        ptr = head

        while ptr != None:
            nums.append(ptr.val)
            ptr = ptr.next
        
        # Alternate start-end
        ptr = head
        side = 'left'

        while len(nums) > 0:
            if side == 'left':
                ptr.val = nums.popleft()
                ptr = ptr.next
                side = 'right'

            else:
                ptr.val = nums.pop()
                ptr = ptr.next
                side = 'left'


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
        
        # Find the start of the second half
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        prev, cur = None, slow
        
        while cur:
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode

        # Criss-cross alternate
        head1, head2 = head, prev
        
        while head1 and head2:
            next1, next2 = head1.next, head2.next

            # Skip the last node since it's a dupe
            if not next1 or not next2: break

            head1.next = head2
            head1 = next1

            head2.next = head1
            head2 = next2

