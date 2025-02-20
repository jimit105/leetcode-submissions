# Time:
# Constructor: O(n)
# fetch: O(n)

class MRUQueue:

    def __init__(self, n: int):
        self.queue = list(range(1, n + 1))
        

    def fetch(self, k: int) -> int:
        element = self.queue[k - 1]
        self.queue.pop(k - 1)
        self.queue.append(element)
        return element

        


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)
