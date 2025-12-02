# Approach: Hash Table + Geometry Mathematics
# Time: O(n)
# Space: O(n)

from collections import defaultdict

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        point_num = defaultdict(int)
        mod = 10 ** 9 + 7

        ans, total_sum = 0, 0

        # Count points at each height
        for point in points:
            point_num[point[1]] += 1

        # Calculate trapezoid combinations
        for p_num in point_num.values():
            edge = p_num * (p_num - 1) // 2
            ans = (ans + edge * total_sum) % mod
            total_sum = (total_sum + edge) % mod

        return ans
        
