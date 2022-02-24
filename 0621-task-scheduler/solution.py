from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencies = list(Counter(tasks).values())
        
        frequencies.sort()
        
        f_max = frequencies.pop()
        idle_time = (f_max - 1) * n
        
        while frequencies and idle_time > 0:
            idle_time -= min(f_max - 1, frequencies.pop())
        idle_time = max(0, idle_time)
        
        return idle_time + len(tasks)
        
