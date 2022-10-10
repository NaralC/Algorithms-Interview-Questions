from math import *

class Solution:
    def countPrimes(self, n: int) -> int:
        # Time: O(n)
        # Space: O(n)
        
        # If the input is 2 or below, there's no prime number less than it
        if n <= 2:
            return 0
        
        # Solution:
        # Sieve of Eratosthenes -> basically cross out all multiples of a prime when you first encounter the prime
        prime = [True for _ in range(n)]
        prime[0] = prime[1] = False # 0 and 1 aren't prime
        
        for num in range(2, int(sqrt(n)) + 1):
            if prime[num]:
                for multiple in range(num * num, n, num):
                    prime[multiple] = False
        
        # Count the number of primes
        count = 0
        
        for isPrime in prime:
            if isPrime: count += 1
        
        return count
