# Approach 2: Double ended queue

# Time: O(1)
# Space: O(n), n = size of moving window

from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.window_sum = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        count = len(self.queue)
        tail = self.queue.popleft() if count > self.size else 0

        self.window_sum = self.window_sum - tail + val

        return self.window_sum / min(self.size, count)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
