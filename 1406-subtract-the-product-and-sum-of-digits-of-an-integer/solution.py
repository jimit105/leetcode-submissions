class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        sum_ = 0
        
        while n > 0:
            last_digit = n % 10
            
            prod *= last_digit
            sum_ += last_digit
            
            n //= 10
            
        return prod - sum_
        
