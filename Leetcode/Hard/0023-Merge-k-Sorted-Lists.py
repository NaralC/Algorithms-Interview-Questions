from heapq import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Time: O(nlogk) where n = total numbers of nodes
        # Space: O(k)
        
        # Retrieve the tail of each list
        minHeap = []
        
        for idx in range(len(lists)):
            if lists[idx]:
                heappush(minHeap, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        
        # Construct a new list by pulling each tail in ascending order
        dummy = ListNode()
        ptr = dummy
        
        while len(minHeap):
            # Make a new node out of the smallest value
            val, idx = heappop(minHeap)
            
            ptr.next = ListNode(val)
            ptr = ptr.next
            
            # Move on from this value, retrieve a new one
            if lists[idx]:
                heappush(minHeap, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        
        return dummy.next