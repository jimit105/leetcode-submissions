# Approach 1: Variant of Binary Search

# Time: O(n), Average = O(log n)
# Space: O(1)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        while high > low:
            pivot = (high + low) // 2
            if nums[pivot] < nums[high]:
                high = pivot
            elif nums[pivot] > nums[high]:
                low = pivot + 1
            else:
                high -= 1

        return nums[low]

