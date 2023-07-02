# Approach: Backtracking

class Solution:
    def __init__(self) -> None:
        self.ans = 0

    def helper(self, start, requests, indegree, n, count) -> None:
        if start == len(requests):
            for i in range(n):
                if indegree[i] != 0:
                    return
            self.ans = max(self.ans, count)
            return

        # Take
        indegree[requests[start][0]] -= 1
        indegree[requests[start][1]] += 1
        self.helper(start + 1, requests, indegree, n, count + 1)

        # Don't Take
        indegree[requests[start][0]] += 1
        indegree[requests[start][1]] -= 1
        self.helper(start + 1, requests, indegree, n, count)

    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        indegree = [0] * n
        self.helper(0, requests, indegree, n, 0)
        return self.ans
