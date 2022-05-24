class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # Time: O(n)
        # Space: O(1)
        
        p1 = p2 = 0
        
        while p1 < len(word) and p2 < len(abbr):
            # p2 is on an alphabet
            if abbr[p2].isalpha():
                if word[p1] != abbr[p2]:
                    return False
                
                p1 += 1
                p2 += 1
            
            # p2 is on a number - find out the whole number
            else:
                # Handle leading zeroes
                if abbr[p2] == '0':
                    return False
                
                num = '0'
                
                while p2 < len(abbr) and abbr[p2].isnumeric():
                    num += abbr[p2]
                    p2 += 1
                
                p1 += int(num)
        
        # Both ptrs have to be simultaneously out of bounds
        # '==' to handle cases like ('a', '2')
        return p1 == len(word) and p2 == len(abbr)