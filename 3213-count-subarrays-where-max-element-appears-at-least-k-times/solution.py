# Approach 1: Sliding Window

# Time: O(n)
# Space: O(1)

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_elem = max(nums)
        ans = start = max_elem_in_window = 0

        for end in range(len(nums)):
            if nums[end] == max_elem:
                max_elem_in_window += 1
            while max_elem_in_window == k:
                if nums[start] == max_elem:
                    max_elem_in_window -= 1
                start += 1
            ans += start

        return ans
        
