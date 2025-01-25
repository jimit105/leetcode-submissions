# Approach: Sliding Window

# Time: O(n)
# Space: O(1)

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zeros_count = 0
        max_consecutive = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros_count += 1
        
            # If we have more zeros than allowed, shrink the window from the left
            while zeros_count > k:
                if nums[left] == 0:
                    zeros_count -= 1
                left += 1

            max_consecutive = max(max_consecutive, right - left + 1)

        return max_consecutive
