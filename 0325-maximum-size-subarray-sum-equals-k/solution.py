# Approach: Prefix Sum + Hash Map

# Time: O(n)
# Space: O(n)

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix_sum = longest_subarray = 0
        indices = {}

        for i, num in enumerate(nums):
            prefix_sum += num

            if prefix_sum == k:
                longest_subarray = i + 1

            if prefix_sum - k in indices:
                longest_subarray = max(longest_subarray, i - indices[prefix_sum - k])

            if prefix_sum not in indices:
                indices[prefix_sum] = i

        return longest_subarray
        
