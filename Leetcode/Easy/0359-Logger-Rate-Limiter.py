class Logger:
    #Time: O(1)
    #Space: O(n)

    def __init__(self):
        self.lastSent = dict() #{message : latest timestamp}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        #Message never received before
        if message not in self.lastSent:
            self.lastSent[message] = timestamp
            return True
        
        #Message allowed to be sent back
        if timestamp >= self.lastSent[message] + 10:
            self.lastSent[message] = timestamp
            return True
        
        #Message not allowed to be sent back
        return False

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)