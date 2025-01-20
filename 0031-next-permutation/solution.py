# Approach 2: Single Pass Approach

# Time: O(n)
# Space: O(1)

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Step 1: Find the first pair from right where nums[i] < nums[i+1]
        i = len(nums) - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1

        if i >= 0:
             # Step 2: Find the smallest number greater than nums[i] to its right
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1

            # Step 3: Swap nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]

        # Step 4: Reverse the subarray after position i
        nums[i + 1 :] = reversed(nums[i + 1 :])

