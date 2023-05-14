# Approach 1: DP with Bitmasking (Recursive)

import math

class Solution:
    def backtrack(self, nums: List[int], mask: int, pairs_picked: int, memo: List[int]) -> int:

        # All numbers picked
        if 2 * pairs_picked == len(nums):
            return 0

        # Already solved this sub-problem
        if memo[mask] != -1:
            return memo[mask]

        max_score = 0

        # Iterate on 'nums' array to pick the first and second number of the pair
        for first_index in range(len(nums)):
            for second_index in range(first_index + 1, len(nums)):
                # If the numbers are same, or already picked, then we move to next number
                if (mask >> first_index) & 1 == 1 or (mask >> second_index) & 1 == 1:
                    continue
                
                # Both numbers are marked as picked in this new mask.
                new_mask = mask | (1 << first_index) | (1 << second_index)

                # Calculate score of current pair of numbers, and the remaining array
                curr_score = (pairs_picked + 1) * math.gcd(nums[first_index], nums[second_index])

                remaining_score = self.backtrack(nums, new_mask, pairs_picked + 1, memo)

                max_score = max(max_score, curr_score + remaining_score)

        memo[mask] = max_score
        return max_score


    def maxScore(self, nums: List[int]) -> int:
        memo_size = 1 << len(nums) # 2 ^ len(nums)
        memo = [-1] * memo_size
        return self.backtrack(nums, 0, 0, memo)
