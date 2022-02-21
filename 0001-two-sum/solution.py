# Approach 3 - One-pass Hash Table

# Time: O(N)
# Space: O(N)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict() # value: index
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            
            hashmap[nums[i]] = i
