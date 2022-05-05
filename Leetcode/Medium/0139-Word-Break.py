class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Time: O(n * len(wordDict) * longest word)
        # Space: O(n)
        
        dp = [False] * (len(s) + 1)
        
        for word in wordDict:
            if word == s[:len(word)]:
                dp[len(word)] = True
        
        for idx in range(len(dp)):
            if dp[idx]:
                for word in wordDict:
                    if idx - 1 + len(word) < len(s) and word == s[idx : idx + len(word)]:
                        dp[idx + len(word)] = True
        
        return dp[-1]