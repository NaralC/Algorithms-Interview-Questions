# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        return greedy(n)
    
def greedy(n):
    #Time: O(n)
    #Space: O(1)
    
    #Greedily pick out one candidate since there's exactly one celebrity
    candidate = 0
    
    for idx in range(n):
        if knows(candidate, idx):
            candidate = idx
    
    #Double check the candidate
    for idx in range(n):
        if candidate == idx:
            continue
        
        #The celebrity must not know anyone but everyone must know them
        if knows(candidate, idx) or not knows(idx, candidate):
            return -1
    
    return candidate
    
        
def utilizeStack(n):
    #Time: O(n)
    #Space: O(n)

    #Put everyone into a stack
    stack = [idx for idx in range(n)]

    #Compare the top most 2 person with each other, and only keep potential candidates
    while len(stack) >= 2:
        a = stack.pop()
        b = stack.pop()

        if knows(a, b):
            stack.append(b)
        else:
            stack.append(a)

    #Double check the candidate
    candidate = stack.pop()

    for idx in range(n):
        if candidate == idx:
            continue

        #The celebrity must not know anyone but everyone must know them
        if knows(candidate, idx) or not knows(idx, candidate):
            return -1

    return candidate