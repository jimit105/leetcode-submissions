# Approach 2: Hashtable

# m = size of all incoming messages
# Time: O(1)
# Space: O(m)

class Logger:

    def __init__(self):
        self.msg_dict = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.msg_dict:
            self.msg_dict[message] = timestamp
            return True

        if timestamp - self.msg_dict[message] >= 10:
            self.msg_dict[message] = timestamp
            return True
        else:
            return False
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
