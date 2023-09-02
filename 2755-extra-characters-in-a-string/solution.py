# Approach 1: Top Down Dynamic Programming with Substring Method

# Time: O(N^3)

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n, dict_set = len(s), set(dictionary)

        @cache
        def dp(start):
            if start == n:
                return 0

            ans = dp(start + 1) + 1
            for end in range(start, n):
                curr = s[start : end + 1]
                if curr in dict_set:
                    ans = min(ans, dp(end + 1))

            return ans

        return dp(0)
        
