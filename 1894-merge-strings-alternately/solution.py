# Approach 2: One Pointer

# Time: O(m + n)
# Space: O(1)

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        max_length = max(len(word1), len(word2))
        for i in range(max_length):
            if i < len(word1):
                result += word1[i]
            if i < len(word2):
                result += word2[i]

        return result
