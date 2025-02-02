# Approach 2: Two Pointers

# Time: O(n log n)

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        answer = -1
        left, right = 0, len(nums) - 1

        while left < right:
            total = nums[left] + nums[right]
            if total < k:
                answer = max(answer, total)
                left += 1
            else:
                right -= 1

        return answer
        
