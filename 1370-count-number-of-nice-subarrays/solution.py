# Approach 1: Hashing

# Time: O(n)
# Space: O(n)

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        subarrays = 0
        prefix_sum = {curr_sum : 1}

        for num in nums:
            curr_sum += num % 2
            if curr_sum - k in prefix_sum:
                subarrays += prefix_sum[curr_sum - k]
            prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1

        return subarrays
        
