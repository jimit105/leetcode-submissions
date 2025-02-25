# Approach 3: Prefix Sum with Odd-Even Counting

# Time: O(n)
# Space: O(1)

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        count = prefix_sum = 0

        odd_count = 0
        even_count = 1 # even_count starts as 1 since the initial sum (0) is even

        for num in arr:
            prefix_sum += num
            # If current prefix sum is even, add the number of odd subarrays
            if prefix_sum % 2 == 0:
                count += odd_count
                even_count += 1
            
            # If current prefix sum is odd, add the number of even subarrays
            else:
                count += even_count
                odd_count += 1

            count %= MOD

        return count

        
