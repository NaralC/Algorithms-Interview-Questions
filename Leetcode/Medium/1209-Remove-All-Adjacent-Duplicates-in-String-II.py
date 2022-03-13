class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        #Time: O(n)
        #Space: O(n)
        #[['a', 2], ['b', 3], ['d', 4]] with k = 3 -> 'aad'
        
        stack = [] #[char, frequency]
        
        for char in s:
            #Increment a duplicate's count should another one show up
            if len(stack) and stack[-1][0] == char:
                stack[-1][1] += 1
            
            #Proceed normally if two different characters stack up
            else:
                stack.append([char, 1])
                
            #If a set of duplicates reach the limit, pop them out
            #Should be put here instead of on top to check the last chunk of string
            if len(stack) and stack[-1][1] == k:
                stack.pop()

        return ''.join([char * freq for char, freq in stack])