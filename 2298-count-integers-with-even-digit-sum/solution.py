class Solution:
    def sum_digits(self, num):
        return 0 if num == 0 else int(num % 10) + self.sum_digits(num // 10)
    
    def countEven(self, num: int) -> int:
        count = 0
        for i in range(1, num + 1):
            if self.sum_digits(i) % 2 == 0:
                count += 1
        return count
        
        
    
