# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #Land a ptr in the second half of the linked list
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
        
        #Check node by node to check whether the list is palindrome
        while previous:
            if previous.val != head.val:
                return False
            
            previous = previous.next
            head = head.next
        
        return True