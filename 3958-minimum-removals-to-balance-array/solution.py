# Approach: Sorting + Two Pointers

# Time: O(n log n)
# Space: O(log n) # Stack space for sorting

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()

        ans = n # Start with worst case; remove all elements
        right = 0

        for left in range(n):
            while right < n and nums[right] <= nums[left] * k:
                right += 1 # Expland right pointer as far as possible
            
            ans = min(ans, n - (right - left))

        return ans

