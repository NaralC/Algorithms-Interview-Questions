class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        #Time: O(n)
        #Space: O(n)
        
        #Judge should have exactly (n - 1) trusts
        #Return -1 if there are multiple candidates who meet this criteria
        #Continue to see if the potential judge trusts anyone, if yes -> return -1
        #If no, return the idx that potential judge
        
        #Track how many times a person is trusted/gives out trusts
        #The first idx is just a dummy for convenience sake
        freq = [0 for _ in range(n + 1)]
        for pair in trust:
            give, receive = pair
            freq[give] -= 1
            freq[receive] += 1
        
        #The judge must have (n - 1) trusts and trusts nobody -> his score must be exactly (n - 1)
        for idx in range(1, n + 1):
            if freq[idx] == n - 1:
                return idx
        
        return -1
            