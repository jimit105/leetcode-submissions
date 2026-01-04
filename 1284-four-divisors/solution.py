# Approach: Square Root Paired Divisor
# Time: O(n * sqrt(max(nums)))
# Space: O(sqrt(max(nums)))

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def get_divisors(n):
            divisors = []
            
            for i in range(1, int(n**0.5) + 1):
                if n % i == 0:
                    divisors.append(i)
                    
                    # Avoid duplicate when i is the square root of n
                    if i != n // i:
                        divisors.append(n // i)
            return divisors

        total = 0
        for num in nums:
            divisors = get_divisors(num)
            if len(divisors) == 4:
                total += sum(divisors)

        return total

