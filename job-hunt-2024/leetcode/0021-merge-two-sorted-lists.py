# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Time: O(n + m)
        # Space: O(n + m)

        l1, l2 = list1, list2
        output = ListNode()
        outputHead = output

        # Do the switcheroo
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                newNode = ListNode(l1.val)
                output.next = newNode
                output = output.next
                l1 = l1.next

            else:
                newNode = ListNode(l2.val)
                output.next = newNode
                output = output.next
                l2 = l2.next

        # Join the other list
        if l1: output.next = l1
        elif l2: output.next = l2

        return outputHead.next
