# Approach 1: Storing indices for all letters

# Time: O(n), n = length of word
# Space: O(1), constant space for 26 letters

class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        key_indices = {char: idx for idx, char in enumerate(keyboard)}

        prev_idx = 0
        result = 0

        for char in word:
            result += abs(key_indices[char] - prev_idx)
            prev_idx = key_indices[char]

        return result
