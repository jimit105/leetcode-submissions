# Approach: Record the Start and End Positions

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        last_lower = {}
        first_upper = {}

        for i, c in enumerate(word):
            if c.islower():
                last_lower[c] = i
            else:
                if c not in first_upper:
                    first_upper[c] = i

        ans = 0
        for c in string.ascii_lowercase:
            if (c in last_lower
                and c.upper() in first_upper
                and last_lower[c] < first_upper[c.upper()]):
                ans += 1

        return ans
        
