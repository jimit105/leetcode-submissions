# Approach 2 - Regex

# Space: O(1)

import re

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return re.fullmatch(r"[A-Z]*|.[a-z]*", word)
