# Approach 2: Two Pointer

# Time: O(n log n)
# Space: O(n)

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        return self.lower_bound(nums, upper + 1) - self.lower_bound(nums, lower)

    # Calculate the number of pairs with sum less than `value`.
    def lower_bound(self, nums, value):
        left, right = 0, len(nums) - 1
        result = 0

        while left < right:
            if nums[left] + nums[right] < value:
                # If sum is less than value, add the size of window to result and move to the next index
                result += right - left
                left += 1
            else:
                # Otherwise, shift the right pointer backwards, until we get a valid window.
                right -= 1

        return result
        
