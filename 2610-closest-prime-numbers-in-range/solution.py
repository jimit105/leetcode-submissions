# Approach 1: Sieve of Eratosthenes

# Time: O(R log(log R) + R - L)
# Space: O(R)

class Solution:
    def _sieve(self, upper_limit):
        sieve = [True] * (upper_limit + 1)
        sieve[0] = sieve[1] = False # 0 and 1 are not prime

        for number in range(2, int(upper_limit ** 0.5) + 1):
            if sieve[number]:
                # Mark all multiple of `number` as non-prime
                for multiple in range(number * number, upper_limit + 1, number):
                    sieve[multiple] = False
        
        return sieve

    def closestPrimes(self, left: int, right: int) -> List[int]:
        sieve_array = self._sieve(right)

        prime_numbers = [num for num in range(left, right + 1) if sieve_array[num]]

        # Find closest prime pair
        if len(prime_numbers) < 2:
            return -1, -1

        min_diff = float('inf')
        closest_pair = (-1, -1)

        for index in range(1, len(prime_numbers)):
            diff = prime_numbers[index] - prime_numbers[index - 1]
            if diff < min_diff:
                min_diff = diff
                closest_pair = prime_numbers[index - 1], prime_numbers[index]

        return closest_pair
        
