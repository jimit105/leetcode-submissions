# Approach: Brute Force

# Time: O(n^2)
# Space: O(n)

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0

        for i in range(n):
            odd = set()
            even = set()

            for j in range(i, n):
                if nums[j] % 2 == 0:
                    even.add(nums[j])
                else:
                    odd.add(nums[j])

                if len(odd) == len(even):
                    max_len = max(max_len, j - i + 1)

        return max_len
        
