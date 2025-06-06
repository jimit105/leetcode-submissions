# Approach: Greedy + Stack

# Z = size of character set, n = len(s)
# Time: O(n + Z)
# Space: O(n)

from collections import Counter

class Solution:
    def robotWithString(self, s: str) -> str:
        cnt = Counter(s)
        stack = []
        res = []
        minChar = 'a'

        for c in s:
            stack.append(c)
            cnt[c] -= 1
            while minChar != 'z' and cnt[minChar] == 0:
                minChar = chr(ord(minChar) + 1)

            while stack and stack[-1] <= minChar:
                res.append(stack.pop())

        return ''.join(res)

        
