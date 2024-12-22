# Approach 1: Prefix Sum

# Time: O(n)
# Space: O(n)

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        total_count = 0
        curr_sum = 0
        sum_freq = {0 : 1} # {prefix_sum : frequency}

        for num in nums:
            curr_sum += num
            if curr_sum - goal in sum_freq:
                total_count += sum_freq[curr_sum - goal]
            
            sum_freq[curr_sum] = sum_freq.get(curr_sum, 0) + 1

        return total_count


        
