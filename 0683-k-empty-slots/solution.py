# Approach 1: Insert Into Sorted Structure

import bisect

class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        active = []

        for day, bulb in enumerate(bulbs, 1):
            i = bisect.bisect(active, bulb)
            for neighbor in active[i - (i > 0) : i + 1]:
                if abs(neighbor - bulb) - 1 == k:
                    return day
            active.insert(i, bulb)

        return -1
