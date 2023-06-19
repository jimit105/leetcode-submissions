# Approach 1: Prefix Sum

# Time: O(N)
# Space: O(1)

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr_altitude = 0
        highest_point = curr_altitude

        for altitude_gain in gain:
            curr_altitude += altitude_gain
            highest_point = max(highest_point, curr_altitude)

        return highest_point
