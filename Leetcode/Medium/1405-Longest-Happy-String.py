class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # Time: O(n) while n is the total frequency of all 3 characters
        # Space: O(n)
        
        output = []
        flagA, flagB, flagC = 0, 0, 0 # Track the last two chars in output string
        
        # Greedily append the most frequent char to output (keep doing so if it doesn't exceed the quota)
        for _ in range(a + b + c):
            maxCount = max(a, b, c)
            
            if (maxCount == a and flagA < 2) or (flagB == 2 and a) or (flagC == 2 and a):
                output.append('a')
                a -= 1
                flagA += 1
                flagB, flagC = 0, 0
                
            elif (maxCount == b and flagB < 2) or (flagA == 2 and b) or (flagC == 2 and b):
                output.append('b')
                b -= 1
                flagB += 1
                flagA, flagC = 0, 0
            
            elif (maxCount == c and flagC < 2) or (flagB == 2 and c) or (flagA == 2 and c):
                output.append('c')
                c -= 1
                flagC += 1
                flagA, flagB = 0, 0
        
        return ''.join(output)


# Alternate solution which uses a max heap (still can't comprehend this one)
# from heapq import *

# class Solution:
#     def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
#         # Let chars with higher counts rise to top
#         maxHeap = []
        
#         for count, char in [(a, 'a'), (b, 'b'), (c, 'c')]:
#             # Python's heap is min, so we gotta invert the values to make it max
#             if count > 0:
#                 heappush(maxHeap, (-count, char))
        
#         # Greedily use up chars with higher count first
#         output = []
        
#         while len(maxHeap):
#             pair = heappop(maxHeap)
#             count, char = -pair[0], pair[1]
            
#             # Append the char into the output
#             if len(output) >= 2 and output[-1] == output[-2] == char:
#                 if not maxHeap: break
                
#                 pairExtra = heappop(maxHeap)
#                 countExtra, charExtra = -pairExtra[0], pairExtra[1]
                
#                 output.append(charExtra)
#                 countExtra -= 1
#                 if countExtra: heappush(maxHeap, (-countExtra, charExtra))
                
#             else:
#                 output.append(char)
#                 count -= 1
            
#             # Put the char back into the heap
#             if count:
#                 heappush(maxHeap, (-count, char))
            
#         return ''.join(output)