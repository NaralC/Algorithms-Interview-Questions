# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Time: O(n)
        # Space: O(1)

        #       t
        #             h
        #   1 <- 2 -> 3 -> 4 -> 5

        if head == None: return

        # Start by having head a step ahead of tail
        tail, head = None, head

        while head != None:
            nextNode = head.next

            # Make head point to tail
            head.next = tail

            # Move both forward
            tail = head
            head = nextNode

        return tail
