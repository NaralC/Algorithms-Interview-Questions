# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        return twoPointers(headA, headB)

def twoPointers(headA, headB):
    #Time: O(m + n) where m = number of nodes in headA, n = number of nodes in headB
    #Space: O(1)
    ptrA, ptrB = headA, headB

    while ptrA != ptrB:
        if ptrA: ptrA = ptrA.next
        else: ptrA = headB #Loop through the other list

        if ptrB: ptrB = ptrB.next
        else: ptrB = headA #Loop through the other list
    
    return ptrA or ptrB #We can return either one of them since they run in parallel