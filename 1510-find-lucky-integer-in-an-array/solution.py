# Approach 3: Counter

# Time: O(n)
# Space: O(n)

from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counts = Counter(arr)
        lucky_num = -1

        for num, count in counts.items():
            if num == count:
                lucky_num = max(lucky_num, num)

        return lucky_num
        
