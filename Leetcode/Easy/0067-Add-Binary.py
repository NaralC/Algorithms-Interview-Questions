class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #Time: O(max(a, b))
        #Space: O(max(a, b))
        #Same as idea as 'Add Two Numbers'
        
        a, b = list(a), list(b)
        output, carry = '', 0
        
        while a or b or carry:
            if len(a):
                carry += int(a.pop())
            if len(b):
                carry += int(b.pop())
            
            output = str(carry % 2) + output
            carry = carry // 2

        # while carry or a or b:
        #     val1 = a.pop() if len(a) else 0
        #     val2 = b.pop() if len(b) else 0
        #     carry += int(val1) + int(val2)
            
        #     output = str(carry % 2) + output
        #     carry //= 2
            
        return output