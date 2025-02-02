# Approach 3: Two Pointers

# Time: O(n ^ 2)
# Space: O(1)

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return 0

        nums.sort()
        count = 0
        n = len(nums)

        # Fix the first element and use two pointers for the remaining elements
        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]

                if curr_sum < target:
                    # All numbers between left and right will also work with left
                    # because array is sorted and we want sum < target
                    count += right - left
                    left += 1
                else:
                    right -= 1

        return count

