class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        additional_chars = len(s) % k
        if additional_chars != 0:
            additional_chars = k - additional_chars
        s += fill * additional_chars
          
        return [s[i: i+k] for i in range(0, len(s), k)]
        
