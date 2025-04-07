# Approach 2: Top Down Dynamic Programming - Memoization

# n = len(nums), m = subset_sum
# Time: O(m * n)
# Space: O(m * n)

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @lru_cache(maxsize = None)
        def dfs(nums, n, subset_sum):
            if subset_sum == 0:
                return True
            if n == 0 or subset_sum < 0:
                return False
            result = (dfs(nums, n - 1, subset_sum - nums[n - 1]) or 
                    dfs(nums, n - 1, subset_sum))
            return result

        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False

        subset_sum = total_sum // 2
        n = len(nums)
        return dfs(tuple(nums), n - 1, subset_sum)
