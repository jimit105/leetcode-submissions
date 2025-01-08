# Approach 1: Optimized Brute Force

# Time: O(n^3)
# Space: O(n^3)

class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        n = len(s)
        valid_substrings = set()

        for start in range(n):
            digit_freq = [0] * 10 # Frequency array for digits 0-9

            for end in range(start, n):
                digit_freq[ord(s[end]) - ord('0')] += 1

                # Variable to store the frequency all digits must match
                common_freq = 0
                is_valid = True

                for count in digit_freq:
                    if count == 0:
                        continue # Skip digits not in the substring
                    if common_freq == 0:
                        # First digit found, set common_frequency
                        common_freq = count
                    if common_freq != count:
                        # Mismatch in frequency, mark as invalid
                        is_valid = False
                        break

                if is_valid:
                    substring = s[start : end + 1]
                    valid_substrings.add(substring)

        return len(valid_substrings)

