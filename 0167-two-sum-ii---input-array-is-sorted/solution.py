# Approach 1 - Two Pointers

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left, right = 0, n - 1
        
        while left < right:
            sum_ = numbers[left] + numbers[right]
            
            if sum_ == target:
                return [left+1, right+1]
            elif sum_ < target:
                left += 1
            else:
                right -= 1
                
        return [-1, 1]
        
