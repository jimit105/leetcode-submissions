# Approach 1: Sort By Custom Comparator: Built-in

# Time: O(n log n)
# Space: O(n)

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key = lambda num: (num.bit_count(), num))
        return arr
