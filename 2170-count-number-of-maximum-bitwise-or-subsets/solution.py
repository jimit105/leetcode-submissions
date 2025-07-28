# Approach 1: Recursion

# Time: O(2^n)
# Space: O(n)

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or_value = 0
        for num in nums:
            max_or_value |= num
        return self._count_subsets(nums, 0, 0, max_or_value)

    def _count_subsets(self, nums, index, current_or, target_or):
        # Base case: reached end of array
        if index == len(nums):
            return 1 if current_or == target_or else 0

        # Don't include current number
        count_without = self._count_subsets(nums, index + 1, current_or, target_or)

        # Include current number
        count_with = self._count_subsets(nums, index + 1, current_or | nums[index], target_or)

        # Return sum of both cases
        return count_without + count_with

