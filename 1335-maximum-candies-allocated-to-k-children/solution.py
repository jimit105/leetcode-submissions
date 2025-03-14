# Approach: Binary Search on The Answer

# n = len(candies), m = max(candies)
# Time: O(n log m)
# Space: O(1)

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        max_candies_in_pile = max(candies)

        left = 0
        right = max_candies_in_pile

        while left < right:
            mid = (left + right + 1) // 2

            if self._can_allocate_candies(candies, k, mid):
                # If possible, move to the upper half to search for a larger number
                left = mid
            else:
                right = mid - 1

        return left

    def _can_allocate_candies(self, candies, k, num_of_candies):
        max_num_of_children = 0

        for pile in candies:
            max_num_of_children += pile // num_of_candies

        return max_num_of_children >= k
