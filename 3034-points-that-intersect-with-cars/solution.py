# Time: O(n * m), n = no. of cars, m = max range of any car
# Space: O(p), p = unique points covered by all cars

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        covered_points = set()

        for start, end in nums:
            for point in range(start, end + 1):
                covered_points.add(point)

        return len(covered_points)
