# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Time: O(n)
        # Space: O(k)
        
        # Check if this needs a reverse
        crawl = head
        
        for _ in range(k):
            if not crawl: return head
            crawl = crawl.next
        
        # Reverse the list
        prev, cur = None, head
        
        for _ in range(k):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        # At this point: 
        # - head = old head
        # - prev = new head
        # - cur = head of the next node
        head.next = self.reverseKGroup(cur, k)
        
        return prev
    