class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        
        return greedy(gas, cost)

def greedy(gas, cost):
    #Time: O(n)
    #Space: O(1)
    #1) If we move to some value, and the total sum is greater than zero, then it means, that previous values did bring some value to the outcome
    #2) If there's a solution, then it has to be the smallest possible value, as it's where values start to stack up
    
    tank, output = 0, 0
    
    for candidate in range(len(gas)):
        tank += gas[candidate] - cost[candidate]
        
        #Not a valid starting city, reset the tank and move onto the next city
        if tank < 0:
            tank = 0
            output = candidate + 1 
            
    return output
    
def bruteForce(gas, cost): #TLE
    #Time: O(n^2)
    #Space: O(1)
    #Trying out every single starting city and all cities in the way, hence the nested loop
    
    for start in range(len(gas)):
        tank = 0
        
        for current in range(start, start + len(gas)):
            if tank < 0:
                break
            
            current %= len(gas)
            tank += gas[current] - cost[current]
        
        if tank >= 0:
            return start
    
    return -1
        