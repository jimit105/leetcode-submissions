# Approach 1: Greedy Way (Hash Table)

# Time: O(n)

class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}

        for c in s:
            freq[c] = freq.get(c, 0) + 1

        res = 0
        has_odd_freq = False

        for f in freq.values():
            if (f % 2) == 0:
                res += f

            else:
                # If the frequency is odd, one occurrence of the
                # character will remain without a match
                res += f - 1
                has_odd_freq = True

        # If has_odd_frequency is true, we have at least one unmatched
        # character to make the center of an odd length palindrome.
        if has_odd_freq:
            return res + 1

        return res
        
