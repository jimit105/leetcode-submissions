# Approach 1: Sorting + Binary Search

# Time: O((m + n) * log m)
# Space: O(m)

import math
import bisect

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        answer = []

        m = len(potions)
        max_potion = potions[m - 1]

        for spell in spells:
            min_potion = math.ceil(success / spell)

            if min_potion > max_potion:
                answer.append(0)
                continue

            index = bisect.bisect_left(potions, min_potion)
            answer.append(m - index)

        return answer
