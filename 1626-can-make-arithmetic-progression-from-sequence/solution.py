# Approach 2: Set

# Time: O(n)
# Space: O(n)

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        min_value, max_value = min(arr), max(arr)
        n = len(arr)

        if max_value - min_value == 0:
            return True
        if (max_value - min_value) % (n - 1):
            return False

        diff = (max_value - min_value) // (n - 1)
        number_set = set()

        for a in arr:
            if (a - min_value) % diff:
                return False
            number_set.add(a)

        return len(number_set) == n
