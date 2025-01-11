# Approach 1: Count Odd Frequencies

# Time: O(n)
# Space: O(1)

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        if len(s) == k:
            return True

        freq = [0] * 26
        odd_count = 0

        for char in s:
            freq[ord(char) - ord('a')] += 1

        for count in freq:
            if count % 2 == 1:
                odd_count += 1

        return odd_count <= k
        
