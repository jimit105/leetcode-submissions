# Approach: Cumulative Sum (Prefix Sum)

# Time: O(n)
# Space: O(n)

from itertools import accumulate

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        s = list(s)

        # Use accumulate to get cumulative shifts from right to left
    # We reverse the shifts array first, then reverse the result
        cum_shifts = list(accumulate(shifts[::-1]))[::-1]

        for i in range(len(s)):
            new_char = chr((ord(s[i]) - ord('a') + cum_shifts[i]) % 26 + ord('a'))
            s[i] = new_char

        return ''.join(s)
        
