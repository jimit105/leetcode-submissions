# Approach - Greedy

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_jump_end = 0
        farthest = 0
        
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])        
            if i == current_jump_end:
                jumps += 1
                current_jump_end = farthest
                
        return jumps
