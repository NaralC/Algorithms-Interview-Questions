class Node:
    def __init__(self):
        self.children = dict()
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = Node()
        
    def add(self, word):
        cur = self.root
        
        for char in word:
            if char not in cur.children:
                cur.children[char] = Node()
            
            cur = cur.children[char]
        
        cur.endOfWord = True
    
    def search(self, word, startNode = None):
        cur = self.root if not startNode else startNode
        
        for idx, char in enumerate(word):
            if char in cur.children or char == '.':
                if char in cur.children:
                    cur = cur.children[char]
                    continue
                
                for child in cur.children:
                    if self.search(word[idx + 1:], cur.children[child]):
                        return True
            
            return False
        
        return cur.endOfWord
        

class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        self.trie.add(word)

    def search(self, word: str) -> bool:
        return self.trie.search(word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)