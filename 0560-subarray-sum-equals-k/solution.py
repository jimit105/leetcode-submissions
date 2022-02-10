# Approach 4 - Using Hashmap

# Time: O(N)
# Space: O(N)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        total = 0
                
        hashmap = {} # {sum_i : no. of occurrences of sum_i}
        hashmap[0] = 1
        
        for i in range(len(nums)):
            total += nums[i]
            
            if (total - k) in hashmap.keys():
                count += hashmap.get(total - k)
            hashmap[total] = hashmap.get(total, 0) + 1
            
        return count
        
