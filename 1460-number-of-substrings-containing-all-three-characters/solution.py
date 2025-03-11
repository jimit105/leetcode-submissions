# Approach 1: Sliding Window

# Time: O(n)
# Space: O(1)

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = right = total = 0
        freq = [0] * 3

        while right < len(s):
            freq[ord(s[right]) - ord('a')] += 1

            while self._has_all_chars(freq):
                # All substrings from current window to end are valid
                # Add count of valid substrings
                total += len(s) - right

                # Remove leftmost character and move left pointer
                freq[ord(s[left]) - ord('a')] -= 1
                left += 1

            right += 1

        return total

    def _has_all_chars(self, freq):
        return all(f > 0 for f in freq)


        
