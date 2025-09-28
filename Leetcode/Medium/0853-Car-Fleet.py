class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Time: O(nlogn)
        # Space: O(n)
        
        # Sort the cars by their starting position
        cars = [(pos, sp) for pos, sp in zip(position, speed)]
        cars.sort(reverse = True)
        
        # Go through the cars one by one, starting from the ones closer to target
        stack = [] # Monotonic: keep bigger time needed to reach target at the bottom
        
        for pos, sp in cars:
            timeNeeded = (target - pos) / sp
            
            # If previous car needs more/equal time to reach target, merge them into a fleet
            if len(stack) and stack[-1] >= timeNeeded:
                stack[-1] = max(stack[-1], timeNeeded) # Can't pass a slower car (that needs more time)
            
            else:
                stack.append(timeNeeded)
                

        return len(stack)


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Time: O(nlogn)
        # Space: O(n)

        cars = [(pos, spd) for pos, spd in zip(position, speed)]
        cars.sort(key = lambda x: x[0], reverse = True) # ones closest to target comes first
        fleet = 0
        maxTimeNeeded = 0

        # Iterate from cars that start ahead, see if they bottleneck other cars
        for pos, spd in cars:
            timeNeeded = (target - pos) / spd

            # Merge: current car catches faster ones
            if timeNeeded > maxTimeNeeded:
                maxTimeNeeded = timeNeeded
                fleet += 1

            # Do nothing: current car arrives before ones that are behind
            else: pass

        return fleet
