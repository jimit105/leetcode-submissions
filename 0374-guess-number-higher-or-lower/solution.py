# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

# def get_num(i, j):
#     return (i+j)>>1

class Solution:
    def guessNumber(self, n: int) -> int:
        i, j = 1, n+1
        
        while True:
            num = (i+j)>>1
            pick = guess(num)
            if pick == 0:
                return num
            elif pick == -1:
                j = num
            else:
                i = num
                
        
