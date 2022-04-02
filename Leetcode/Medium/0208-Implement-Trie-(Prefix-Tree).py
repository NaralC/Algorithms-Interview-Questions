class Node():
    def __init__(self):
        self.children = dict()
        self.isEnd = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        current = self.root
        
        for char in word:
            if char not in current.children:
                current.children[char] = Node()
            current = current.children[char]

    def search(self, word: str) -> bool:
        # When we're at the last char/node - check whether it's the end of a word
        # since 'app' would make it through 'apple' but isn't actually the same word
        
        current = self.root
        
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        
        return current.isEnd
    
    def startsWith(self, prefix: str) -> bool:
        # Essentially like the function above but without the need to check for ends of words
        
        current = self.root
        
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)