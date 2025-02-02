# Approach 3: Find Smallest Element

# Time: O(n)
# Space: O(1)

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return True

        inversion_count = 0 # count of pairs where number is greater than next one

        for index in range(1, n):
            if nums[index] < nums[index - 1]:
                inversion_count += 1

        # Check first and last element due to rotation
        if nums[0] < nums[n - 1]:
            inversion_count += 1

        return inversion_count <= 1
        
