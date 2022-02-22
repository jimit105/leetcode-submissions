# Approach 1 - Two Pointers

# Time: O(n^2)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSumII(nums, i, res)
                
        return res
    
    def twoSumII(self, nums, i, res):
        lo = i + 1
        hi = len(nums) - 1
        
        while lo < hi:
            total = nums[i] + nums[lo] + nums[hi]
            if total < 0:
                lo += 1
            elif total > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1
                            
