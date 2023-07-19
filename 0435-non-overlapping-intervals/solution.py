# Approach 1: Greedy

# Time: O(n * log n)
# Space: O(n)

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        ans = 0
        last_end = float('-inf')

        for start, end in intervals:
            if start >= last_end:
                last_end = end
            else:
                ans += 1

        return ans
