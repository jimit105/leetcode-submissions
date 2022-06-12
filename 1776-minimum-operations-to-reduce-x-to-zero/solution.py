# Approach 2 - Two Pointers (Directly)

# Time: O(N)
# Space: O(1)

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        current = sum(nums) # Sum from `nums[0]` to `nums[left - 1]` and `nums[right + 1]` to `nums[last]`
        n = len(nums)
        mini = inf # Minimum length that sums up to x
        left = 0
        
        for right in range(n):
            # sum(nums[0], ..., nums[left]) + sum(nums[right], ..., nums[n-1]) = x
            current -= nums[right]
            
            # If smaller, move `left` to right
            while current < x and left <= right:
                current += nums[left]
                left += 1
                
            # Check if equal
            if current == x:
                mini = min(mini, (n - 1 - right) + left)
                
        return mini if mini != inf else -1
            
        
