# Approach 2: Greedy Bit Manipulation (Counting Ones)
# Time: O(n)
# Space: O(n)

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        ones_cnt = s.count('1')

        return '1' * (ones_cnt - 1) + '0' * (n - ones_cnt) + '1'
        
