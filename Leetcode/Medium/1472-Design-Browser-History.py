class DoublyLinkedList:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.root = DoublyLinkedList(homepage)

    def visit(self, url: str) -> None:
        #This automatically discards the nodes to the right
        nextNode = DoublyLinkedList(url)
        nextNode.left = self.root
        self.root.right = nextNode
        self.root = nextNode

    def back(self, steps: int) -> str:
        #Keep going back x steps or until it's the end of the list
        for _ in range(steps):
            if not self.root.left:
                break
            
            self.root = self.root.left
        
        return self.root.val

    def forward(self, steps: int) -> str:
        #Keep going forward x steps or until it's the end of the list
        for _ in range(steps):
            if not self.root.right:
                break
            
            self.root = self.root.right
        
        return self.root.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)