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
        #Time: O(n)
        #Space: O(1)
        
        #Split the list into halves, while first half >= second in size
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #Reverse the second half
        previous = None
        while slow:
            nextNode = slow.next
            slow.next = previous
            previous = slow
            slow = nextNode
        
        #Reorder the entire list
        first, second = head, previous
        while second.next:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            
            first, second = temp1, temp2