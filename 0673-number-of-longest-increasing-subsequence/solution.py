# Approach 1: Bottom-up Dynamic Programming

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # length[i] represents the length of the LIS ending at index i in the nums array, while count[i] denotes the count of LISs ending at index i
        n = len(nums)
        length = [1] * n
        count = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = 0
                    if length[j] + 1 == length[i]:
                        count[i] += count[j]

        max_length = max(length)
        result = 0

        for i in range(n):
            if length[i] == max_length:
                result += count[i]

        return result
