# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        divideList(head)
        
def iterationStack(head):
    #Time: O(n)
    #Space: O(n)

    stack = []

    while head:
        stack.append(head)
        head = head.getNext()

    while len(stack):
        node = stack.pop()
        node.printValue()
        

def divideList(head):
    #Time: O(n)
    #Space: O(logn) since we supposedly "divided" the list into halves

    #Divide the list into 2 halves with slow and fast ptrs
    #Print the right half first, followed by the left half

    left, right = head, head
    fast = head

    while fast.getNext() and fast.getNext().getNext():
        fast = fast.getNext().getNext()
        right = right.getNext()

    traverse(right, None)
    traverse(left, right)
    
        
def constantSpace(head):
    #Time: O(n^2)
    #Space: O(1)
    
    #Count how many nodes there are, and used a nested loop to print the last node
    #Everytime the end is reached, push the boundary closer to the head

    count = 0
    dummy = head

    while dummy:
        count += 1
        dummy = dummy.getNext()

    while count:
        dummy = head

        for _ in range(count - 1):
            dummy = dummy.getNext()

        dummy.printValue()
        count -= 1
        
        
def traverse(node, stop):
    #Helper function for traversing the list recursively
    
    if node.getNext() == stop:
        node.printValue()
    else:
        traverse(node.getNext(), stop)
        node.printValue()
        
        