# Approach 1 - Dynamic Programming

# Time: O(N)
# Space: O(1)

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        # Since House[1] and House[n] are adjacent, they cannot be robbed together. Therefore, the problem becomes to rob either House[1]-House[n-1] or House[2]-House[n], depending on which choice offers more money.
        return max(self.rob_simple(nums[:-1]), self.rob_simple(nums[1:]))

    
    def rob_simple(self, nums):
        t1, t2 = 0, 0
        for current in nums:
            temp = t1
            t1 = max(current + t2, t1)
            t2 = temp
            
        return t1
