# Approach 3 - One-pass Hash Table

# Time: O(N)
# Space: O(N)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict() # value: index

        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [i, hashmap[complement]]

            hashmap[num] = i

        return []
        
