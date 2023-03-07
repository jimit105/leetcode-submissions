# Approach: Binary Search

# Time: O(n.log(m.k)), n = length of `time` m = upper limit of `totalTrips`, k = max time taken by one trip
# Space: O(1)

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left, right = 1, max(time) * totalTrips

        def is_time_enough(given_time):
            actual_trips = 0
            for t in time:
                actual_trips += given_time // t
            return actual_trips >= totalTrips

        while left < right:
            mid = (left + right) // 2
            if is_time_enough(mid):
                right = mid
            else:
                left = mid + 1

        return left
