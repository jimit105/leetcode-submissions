# Approach 1: Frequency Counter

# Time: O(N)
# Space: O(N)

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq = [0] * (len(nums) + 1)
        res = []

        for i in nums:
            if freq[i] >= len(res):
                res.append([])
            res[freq[i]].append(i)
            freq[i] += 1

        return res
