# Approach 2: Binary Search
# https://leetcode.com/problems/insert-interval/solutions/2914120/insert-intervals/comments/1726090

# Time: O(N)

import bisect

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        position = bisect.bisect(intervals, newInterval)
        intervals.insert(position, newInterval)

        ans = []
        for interval in intervals:
            if not ans or interval[0] > ans[-1][1]: #interval[start] > last_answer[end]
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])   #last_answer[end] = max(last_answer[end], interval[end])

        return ans
                

