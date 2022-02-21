class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #Time: O(n)
        #Space: O(n)
        #Negative asteroids that precede positives one do not collide because 
        #"We are given an array asteroids of integers representing asteroids in a row."
        
        stack = []
        
        for a in asteroids:
            #Thus we only need to check when positive asteroids precede negative ones
            while len(stack) and a < 0 < stack[-1]:
                if abs(a) == stack[-1]:
                    stack.pop()
                    break
                elif abs(a) > stack[-1]:
                    stack.pop()
                else:
                    break

            else:
                stack.append(a)
                
        return stack