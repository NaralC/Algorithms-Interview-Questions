class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        return stack(temperatures)

def noStack(temperatures):
    #Time: O(n)
    #Space: O(1) excluding the output
    output = [0] * len(temperatures)
    
    #Skipping the last ele since it has no days ahead anyways
    for today in range(len(temperatures) - 2, -1, -1):
        nextDays = 1
        
        while nextDays and temperatures[today + nextDays] <= temperatures[today]:
            if output[today + nextDays]:
                nextDays += output[today + nextDays]
            else:
                nextDays = 0
            
        output[today] = nextDays
    
    return output
        
def stack(temperatures):
    # Time: O(n)
    # Space: O(n)

    # Use the top of the stack (warmer temps) to 'crush' colder temps
    stack = [] # contains (idx, temp)
    output = [0] * len(temperatures)

    for curIdx, curTemp in enumerate(temperatures):
        # Current temp is warmer than former one(s)
        while len(stack) and curTemp > stack[-1][1]:
            pastIdx, pastTemp = stack.pop()
            output[pastIdx] = abs(curIdx - pastIdx)
        
        # Current temp is colder than former one
        if not len(stack) or curTemp <= stack[-1][1]:
            stack.append((curIdx, curTemp))

    return output

