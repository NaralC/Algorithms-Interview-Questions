class Node:
    def __init__(self, val, prev, nxt):
        self.val = val
        self.prev = prev
        self.nxt = nxt

class BrowserHistory:
    # Time: O(n)
    # Space: O(n)
    
    # Time: O(1)
    # Space: O(n)
    def __init__(self, homepage: str):
        self.browser = Node(homepage, None, None)
        self.cur_page = self.browser
        
    # Time: O(1)
    # Space: O(1)
    def visit(self, url: str) -> None:
        nxtPage = Node(url, self.cur_page, None)
        self.cur_page.nxt = nxtPage
        self.cur_page = self.cur_page.nxt

    # Time: O(n)
    # Space: O(1)
    def back(self, steps: int) -> str:
        
        while steps > 0 and self.cur_page.prev:
            self.cur_page = self.cur_page.prev
            steps -= 1
            
        return self.cur_page.val

    # Time: O(n)
    # Space: O(1)
    def forward(self, steps: int) -> str:
        
        while steps > 0 and self.cur_page.nxt:
            self.cur_page = self.cur_page.nxt
            steps -= 1
            
        return self.cur_page.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)