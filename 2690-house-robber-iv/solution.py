# Approach: Binary Search

# Time: O(n log n)
# Space: O(1)

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        min_reward, max_reward = 1, max(nums)
        total_houses = len(nums)

        while min_reward < max_reward:
            mid_reward = (min_reward + max_reward) // 2
            possible_thefts = 0

            idx = 0
            while idx < total_houses:
                if nums[idx] <= mid_reward:
                    possible_thefts += 1
                    idx += 2 # Skip next house
                else:
                    idx += 1

            if possible_thefts >= k:
                max_reward = mid_reward
            else:
                min_reward = mid_reward + 1

        return min_reward
