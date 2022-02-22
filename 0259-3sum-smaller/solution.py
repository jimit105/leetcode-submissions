# Approach 3 - Two Pointers

# Time: O(n^2)
# Space: O(1)

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        total = 0
        
        for i in range(len(nums)-1):
            total += self.twoSumSmaller(nums, i + 1, target - nums[i])
            
        return total
    
    def twoSumSmaller(self, nums, start_index, target):
        total = 0
        left, right = start_index, len(nums) - 1
        
        while left < right:
            if nums[left] + nums[right] < target:
                total += right - left
                left += 1
            else:
                right -= 1
                
        return total
        
