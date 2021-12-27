class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        return stack(temperatures)

def noStack(temperatures):
    #Time: O(n)
    #Space: O(1) excluding the output
    output = [0] * len(temperatures)
    
    #Skipping the last element since it has no hotter days anyway
    for today in range(len(temperatures) - 2, -1, -1):
        nextDays = 1
        
        while nextDays and temperatures[today] > temperatures[today + nextDays]:
            if output[today + nextDays]:
                nextDays += output[today + nextDays]
            else:
                nextDays = 0
                
        output[today] = nextDays
    
    return output


        
def stack(temperatures):
    #Time: O(n)
    #Space: O(n)
    output, stack = [0] * len(temperatures), []

    for today, temp in enumerate(temperatures):
        while len(stack) and temp > stack[-1][0]:
            prevDay = stack.pop()[-1] #get the date of the cooler day
            output[prevDay] = today - prevDay #output[prevDay] = warmer date - cooler date

        stack.append([temp, today]) #stack = [[temp, idx]]

    return output
