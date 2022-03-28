from heapq import heappush, heappop

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #Time: O(n * logm) since we insert all nodes into a heap of size m (where m = number of lists) to make comparisons there
        #Space: O(n)
        
        #Main Idea: push each list's tail into a min heap -> pop the smallest node out to form a new list -> move on from that node
        
        #Put each list's tail into a min heap
        minHeap = []
        
        for idx in range(len(lists)):
            if lists[idx]:
                heappush(minHeap, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        
        #Continuously pop the smallest node out, move on from that node by moving through its list, and append a new node into our heap
        dummy = ListNode()
        ptr = dummy
        
        while len(minHeap):
            val, idx = heappop(minHeap)
            
            #Connect to our final list
            ptr.next = ListNode(val)
            ptr = ptr.next
            
            #Move on from the used node
            if lists[idx]:
                heappush(minHeap, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        
        return dummy.next
    
        