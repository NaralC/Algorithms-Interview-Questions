# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        #Time: O(n)
        #Space: O(n)
        
        #Traverse the list to put all numbers into an array
        values = []
        ptr = head
        
        while ptr:
            values.append(ptr.val)
            ptr = ptr.next
        
        #Loop over the list once with a monotonic stack
        output = [0 for _ in range(len(values))]
        stack = [] #[val, idx]
        
        for idx in range(len(values)):
            
            while len(stack) and stack[-1][0] < values[idx]:
                targetIdx = stack.pop()[1]
                output[targetIdx] = values[idx]
            
            stack.append([values[idx], idx])
        
        return output