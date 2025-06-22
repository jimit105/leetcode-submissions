# Time: O(max(n, k))
# Space: O(1)

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        n = len(s)
        curr = 0

        while curr < n:
            res.append(s[curr : curr + k])
            curr += k

        res[-1] += fill * (k - len(res[-1]))
        return res

