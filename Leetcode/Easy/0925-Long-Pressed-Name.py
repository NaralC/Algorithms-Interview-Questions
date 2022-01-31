class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        #Time: O(len(typed))
        #Space: O(1)
        
        #Typed must always be longer than name / If their first characters don't match
        if len(name) > len(typed) or name[0] != typed[0]:
            return False
        
        idx = 0 #idx -> name
        
        for char in typed:
            #Char match -> progress idx
            if idx < len(name) and char == name[idx]:
                idx += 1
                
            #No char match -> check if the current char is not alien to both strings
            elif char != name[idx - 1]:
                return False
        
        return idx >= len(name)