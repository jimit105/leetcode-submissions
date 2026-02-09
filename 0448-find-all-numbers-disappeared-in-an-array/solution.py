# Approach 1: Using Set

# Time: O(n)
# Space: O(n)

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hash_set = set()

        for num in nums:
            hash_set.add(num)

        result = []

        for num in range(1, len(nums) + 1):
            if num not in hash_set:
                result.append(num)

        return result
        
