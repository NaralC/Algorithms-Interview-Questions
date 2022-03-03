# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        #Time: O(n)
        #Space: O(1)
        
        #Reverse the list first, so we can start with the least significant bit
        newHead = reverseList(head)
        
        #Add one to the list, keep going if the number's 9, and stop if otherwise
        ptr = newHead
        
        while ptr:
            if ptr.val == 9:
                ptr.val = 0
            else:
                ptr.val += 1
                return reverseList(newHead)
            
            ptr = ptr.next
        
        #We only reach this iff there's a carry over left in this most significant bit
        #Reverse the list back, and add a node of value one to the front
        output = ListNode(1, reverseList(newHead))
        return output
    
        
def reverseList(head):
    prev = None

    while head:
        nextNode = head.next
        head.next = prev
        prev = head
        head = nextNode

    return prev