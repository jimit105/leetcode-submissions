# Approach: Sorting

# Time: O(n log n)
# Space: O(n)

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        vals = [(i, nums[i]) for i in range(n)]
        vals.sort(key=lambda x: -x[1]) # Sort in descending order of nums
        vals = sorted(vals[:k]) # Pick first k elements and sorted in ascending order by index
        res = [val for idx, val in vals]
        return res
        
