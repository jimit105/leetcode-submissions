# Approach 2: Optimized Recursion

# Time: O(2^n)
# Space: O(n)

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        char_count = [0] * 26
        for char in tiles:
            char_count[ord(char) - ord('A')] += 1

        return self._find_sequences(char_count)

    def _find_sequences(self, char_count):
        total = 0

        for pos in range(26):
            if char_count[pos] == 0:
                continue

            # Add current char and recurse
            total += 1
            char_count[pos] -= 1
            total += self._find_sequences(char_count)
            char_count[pos] += 1

        return total
        
