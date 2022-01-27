# Approach 1 - Bitwise Prefixes in HashSet

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        L = max(nums).bit_length()
        max_xor = 0
        
        for i in range(L)[::-1]:
            max_xor <<= 1
            curr_xor = max_xor | 1
            prefixes = {num >> i for num in nums}
            max_xor |= any(curr_xor ^ p in prefixes for p in prefixes)
            
        return max_xor
            
            
        
