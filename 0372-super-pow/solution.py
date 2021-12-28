class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        b = map(str, b)
        b = int(''.join(b))
        return pow(a, b, 1337)
        
