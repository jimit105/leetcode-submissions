# Approach 1: Backtracking

# Time: O(k ^ n)
# Space: O(k + n)
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        curr = [0] * k
        n = len(cookies)

        def dfs(i, zero_count):
            if n - i < zero_count:
                return float('inf')

            if i == n:
                return max(curr)

            ans = float('inf')
            for j in range(k):
                zero_count -= int(curr[j] == 0)
                curr[j] += cookies[i]

                ans = min(ans, dfs(i + 1, zero_count))

                curr[j] -= cookies[i]
                zero_count += int(curr[j] == 0)

            return ans

        return dfs(0, k)

