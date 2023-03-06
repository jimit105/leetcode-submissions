# Approach 2: Binary Search

# Time: O(log N)
# Space: O(1)

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1

        while left <= right:
            pivot = (left + right) // 2

            if arr[pivot] - pivot - 1 < k:
                left = pivot + 1
            else:
                right = pivot - 1

        return left + k
