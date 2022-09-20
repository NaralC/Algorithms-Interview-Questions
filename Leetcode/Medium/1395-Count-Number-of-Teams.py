class Solution:
    def numTeams(self, rating: List[int]) -> int:
        # Time: O(n^2)
        # Space: O(n)

        teamCount = 0
        greater = [0] * len(rating) # Count of greater numbers after rating[idx]
        smaller = [0] * len(rating) # Count of smaller numbers after rating[idx]
        
        # For each soldier, we search the next greater and smaller
        for idx in range(len(rating)):
            for subIdx in range(idx + 1, len(rating)):
                if rating[idx] < rating[subIdx]:
                    greater[idx] += 1
                    
                elif rating[idx] > rating[subIdx]:
                    smaller[idx] += 1
                   
        # For each soldier, find the last number to make a triplet (by adding on top how many greater/smaller are afterwards)
        for idx in range(len(rating) - 2):
            for subIdx in range(idx + 1, len(rating)):
                if rating[idx] < rating[subIdx]:
                    teamCount += greater[subIdx]
                    
                elif rating[idx] > rating[subIdx]:
                    teamCount += smaller[subIdx]
                
        return teamCount