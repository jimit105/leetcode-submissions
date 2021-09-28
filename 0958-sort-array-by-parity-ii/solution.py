class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even_nums = list(filter(lambda x: x%2 == 0, nums))
        odd_nums = list(filter(lambda x: x%2 != 0, nums))
        
        output = []
        for even, odd in zip(even_nums, odd_nums):
            output.append(even)
            output.append(odd)
            
        del nums, odd_nums, even_nums, even, odd
        return output
        
        
