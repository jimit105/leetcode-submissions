class Solution:
    def bitwiseComplement(self, n: int) -> int:
        num = n.bit_length()
        mask = int(2**num-1) if num > 0 else 1
               
        return n^mask
        
