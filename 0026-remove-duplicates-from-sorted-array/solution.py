# Approach 1: Two indexes approach

# Time: O(n)
# Space: O(1)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        insert_idx = 1

        for i in range(1, size):
            if nums[i - 1] != nums[i]:
                nums[insert_idx] = nums[i]
                insert_idx += 1

        return insert_idx
        
