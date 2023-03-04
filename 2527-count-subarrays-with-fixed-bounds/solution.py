# Approach: Two Pointers

# Time: O(n)
# Space: O(1)

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # min_position, max_position: the MOST RECENT positions of minK and maxK.
        # left_bound: the MOST RECENT value outside the range [minK, maxK].
        answer = 0
        min_position = max_position = left_bound = -1

        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                left_bound = i

            if num == minK:
                min_position = i
            if num == maxK:
                max_position = i

            # The number of valid subarrays equals the number of elements between left_bound and 
            # the smaller of the two most recent positions.
            answer += max(0, min(min_position, max_position) - left_bound)

        return answer
