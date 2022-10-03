from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # Time: O(n + m * length of each word)
        # Space: O(n + m * length of each word)
        count = 0
        chars_count = Counter(chars)

        for word in words:
            if len(word) > len(chars):
                continue

            word_count = Counter(word)
            valid = True

            for char, freq in word_count.items():
                if char not in chars_count or word_count[char] > chars_count[char]:
                    valid = False
                    break
   
            count += len(word) if valid else 0

        return count