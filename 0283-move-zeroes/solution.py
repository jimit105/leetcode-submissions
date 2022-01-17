class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curr_zero = 0 # record the position of zero
        
        if 0 in nums and len(nums) > 1:
            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[i], nums[curr_zero] = nums[curr_zero], nums[i]
                    curr_zero += 1
        
