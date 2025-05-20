# Approach: Difference Array

# n = len(nums), m = len(queries)
# Time: O(n + m)
# Space: O(n)

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        delta_array = [0] * (len(nums) + 1)
        for left, right in queries:
            delta_array[left] += 1
            delta_array[right + 1] -= 1

        operation_count = []
        curr_operations = 0

        for delta in delta_array:
            curr_operations += delta
            operation_count.append(curr_operations)

        for operations, target in zip(operation_count, nums):
            if operations < target:
                return False

        return True
        
