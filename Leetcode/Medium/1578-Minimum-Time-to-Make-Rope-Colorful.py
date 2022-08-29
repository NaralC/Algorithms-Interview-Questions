class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        return greedyStack(colors, neededTime)
    
def greedyStack(colors: str, neededTime: List[int]) -> int:
    # Time: O(n)
    # Space: O(n)

    # Greedy + Stack
    # Traverse through the string, emulate using up the color with lower time needed
    output = 0
    stack = [] # [color, time]

    for color, time in zip(colors, neededTime):
        # Two identical colors, use the one with lower time needed. So the bigger time is kept
        if len(stack) and stack[-1][0] == color:
            output += min(time, stack[-1][1])
            stack[-1][1] = max(time, stack[-1][1])

        else:
            stack.append([color, time])

    return output
    
def greedyConstant(colors: str, neededTime: List[int]) -> int:
    # Time: O(n)
    # Space: O(1)

    # Traverse through the string, emulate using up the color with lower time needed
    output = 0

    for idx in range(1, len(colors)):
        # So the bigger time is kept
        if colors[idx - 1] == colors[idx]:
            output += min(neededTime[idx - 1], neededTime[idx])
            neededTime[idx] = max(neededTime[idx - 1], neededTime[idx])

    return output
    