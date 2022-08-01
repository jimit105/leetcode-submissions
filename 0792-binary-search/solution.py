# Approach 1 - Binary Search

# Time: O(log N)
# Space: O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            elif target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
                
        return -1
        
