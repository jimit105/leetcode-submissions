class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_length = 0
        current_ones = 0
        for num in nums:
            if num == 1:
                current_ones += 1
                max_length = max(max_length, current_ones)
            else:
                current_ones = 0
                
        return max_length
        
