# Approach 1: Hash Table

# Time: O(n)
# Space: O(n)

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res = []
        count = {}

        for x in nums:
            count[x] = count.get(x, 0) + 1
            if count[x] == 2:
                res.append(x)

        return res
        
