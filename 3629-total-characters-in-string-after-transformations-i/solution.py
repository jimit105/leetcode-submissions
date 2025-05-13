# Approach: Recurrence

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10 ** 9 + 7
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        for round in range(t):
            nxt = [0] * 26
            nxt[0] = count[25]
            nxt[1] = (count[25] + count[0]) % MOD

            for i in range(2, 26):
                nxt[i] = count[i - 1]

            count = nxt

        ans = sum(count) % MOD
        return ans
        
