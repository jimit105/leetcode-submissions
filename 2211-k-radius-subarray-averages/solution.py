# Approach 1: Prefix Sum

# Time: O(n)
# Space: O(n)

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums

        n = len(nums)
        averages = [-1] * n

        if 2 * k + 1 > n:
            return averages

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        for i in range(k, n - k):
            left_bound, right_bound = i - k, i + k
            subArray_sum = prefix[right_bound + 1] - prefix[left_bound]
            average = subArray_sum // (2 * k + 1)
            averages[i] = average

        return averages
