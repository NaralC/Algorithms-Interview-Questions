class Solution:
    def originalDigits(self, s: str) -> str:
        #Time: O(n)
        #Space: O(1) since the input is limited to English characters
        
        #Make a dict allocate all characters used by words 'one' to 'nine'
        freq = {}
        
        for char in ["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"]:
            freq[char] = 0
            
        for char in s:
            freq[char] = freq.get(char, 0) + 1
            
        #Count how many times each number can be formed
        count = [0 for _ in range(10)]
        
        count[0] = freq['z']
        count[2] = freq['w']
        count[4] = freq['u']
        count[6] = freq['x']
        count[8] = freq['g']
        
        count[1] = freq['o'] - count[0] - count[2] - count[4]
        count[3] = freq['h'] - count[8]
        count[5] = freq['f'] - count[4]
        count[7] = freq['s'] - count[6]
        count[9] = freq['i'] - count[5] - count[6] - count[8]
        
        #Organize everything into the output
        output = []
        
        for idx in range(10):
            output.append(count[idx] * str(idx))
            
        return ''.join(output)