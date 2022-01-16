# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #Time: O(max(list1, list2))
        #Space: O(max(list1, list2))
        
        ptr1, ptr2 = list1, list2
        newList = ListNode('dummy')
        newHead = newList
        
        while ptr1 or ptr2:
            val1 = ptr1.val if ptr1 else float('inf')
            val2 = ptr2.val if ptr2 else float('inf')
            
            #Smaller values go first
            if val1 < val2:
                newList.next = ListNode(val1)
                ptr1 = ptr1.next if ptr1 else None
            else:
                newList.next = ListNode(val2)
                ptr2 = ptr2.next if ptr2 else None
                
            newList = newList.next
               
        return newHead.next