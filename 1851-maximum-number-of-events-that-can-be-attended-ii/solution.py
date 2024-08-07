# Approach 1: Top Down Dynamic Programming + Binary Search

# Time: O(n * k * log n)
# Space: O(n * k)

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        n = len(events)
        starts = [start for start, end, value in events]
        dp = [[-1] * n for _ in range(k + 1)]

        def dfs(curr_index, count):
            if count == 0 or curr_index == n:
                return 0
            if dp[count][curr_index] != -1:
                return dp[count][curr_index]

            next_index = bisect.bisect_right(starts, events[curr_index][1])
            dp[count][curr_index] = max(dfs(curr_index + 1, count), events[curr_index][2] + dfs(next_index, count - 1))

            return dp[count][curr_index]

        return dfs(0, k)

