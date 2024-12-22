# Approach 2: Sliding Window

# Time: O(n)
# Space: O(1)

class Solution:
    # Helper function to count the number of subarrays with sum at most the given goal
    def sliding_window_at_most(self, nums: List[int], goal: int) -> int:
        start, curr_sum, total_count = 0, 0, 0

        for end in range(len(nums)):
            curr_sum += nums[end]

            # Adjust the window by moving the start pointer to the right
            # until the sum becomes less than or equal to the goal
            while start <= end and curr_sum > goal:
                curr_sum -= nums[start]
                start += 1

            # Update the total count by adding the length of the current subarray
            total_count += end - start + 1

        return total_count


    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.sliding_window_at_most(nums, goal) - self.sliding_window_at_most(nums, goal - 1)
        
