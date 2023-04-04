# Approach: Greedy

# Time: O(n)
# Space: O(26)=O(1)

class Solution:
    def partitionString(self, s: str) -> int:
        last_seen = [-1] * 26
        count = 1
        substring_start = 0

        for i in range(len(s)):
            if last_seen[ord(s[i]) - ord('a')] >= substring_start:
                count += 1
                substring_start = i
            last_seen[ord(s[i]) - ord('a')] = i

        return count
