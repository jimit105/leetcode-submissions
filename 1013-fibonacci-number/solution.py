from functools import lru_cache

class Solution:
    
    @lru_cache
    def fib(self, n: int) -> int:
        return n if n <= 1 else self.fib(n - 2) + self.fib(n - 1)
        
