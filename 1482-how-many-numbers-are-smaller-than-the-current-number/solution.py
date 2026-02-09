# Time: O(n^2)

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        return [sum(x < num for x in nums) for num in nums]
        
