class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #Time: O(n)
        #Space: O(1)
        return forward(nums)
    
def backward(nums):
    goal = len(nums) - 1
    
    for idx in reversed(range(len(nums))):
        #Determine whether this number can reach the goal
        #If yes, that means reaching it == reaching the goal
        if nums[idx] + idx >= goal:
            goal = idx
    
    #Determines whether we can access the goal from the start
    return goal == 0

def forward(nums):
    goal = 0
    
    for idx in range(len(nums)):
        #We've gone pass the max reach
        if idx > goal:
            return False
        
        #Determine the furthest reach for now
        goal = max(goal, nums[idx] + idx)
    
    return True