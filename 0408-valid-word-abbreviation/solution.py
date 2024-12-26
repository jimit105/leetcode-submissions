# Approach: Two Pointers

# Time: O(n)
# Space: O(1)

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0 # i for word, j for abbr

        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
                continue

            if not abbr[j].isdigit():
                return False

            if abbr[j] == '0':
                return False

            # Get the complete number from abbr
            length = 0
            while j < len(abbr) and abbr[j].isdigit():
                length = length * 10 + int(abbr[j])
                j += 1

            # Move word pointer by the length
            i += length

            if i > len(word):
                return False

        return i == len(word) and j == len(abbr)
        
