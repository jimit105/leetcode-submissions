# Approach 1: Find Pivot Index + Binary Search

# Time: O(log n)
# Space: O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1

        # Find the index of the pivot element (the smallest element)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1

        # Binary search over an inclusive range [left_boundary ~ right_boundary]
        def binary_search(left_boundary, right_boundary, target):
            left, right = left_boundary, right_boundary
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        # Binary search over elements on the pivot element's left
        if (answer := binary_search(0, left - 1, target)) != -1:
            return answer

        # Binary search over elements on the pivot element's right
        return binary_search(left, n - 1, target)
        
