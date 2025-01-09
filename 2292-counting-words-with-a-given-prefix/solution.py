# Approach 2: Built-in Methods

# n = length of input array, m = length of the prefix string
# Time: O(m * n)
# Space: O(1)

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(word.startswith(pref) for word in words)
        
