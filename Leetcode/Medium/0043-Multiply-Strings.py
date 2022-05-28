class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Time: O(m * n)
        # Space: O(m + n)
        
        if num1 == '0' or num2 == '0': return '0'
        
        output = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        
        # Pair up each number and multiply them
        for idx1 in range(len(num1)):
            for idx2 in range(len(num2)):
                result = int(num1[idx1]) * int(num2[idx2])
                output[idx1 + idx2] += result # Insert result
                output[idx1 + idx2 + 1] += (output[idx1 + idx2] // 10) # Put carry onto the next cell
                output[idx1 + idx2] %= 10 # Only keep one digit in each index (i.e. cases like '25')
        
        # Get rid of leading zeroes
        output = output[::-1]
        ptr = 0
        
        while ptr < len(output) and output[ptr] == 0:
            ptr += 1
        
        # Convert each element to a string and join them
        return ''.join(str(c) for c in output[ptr:])