# Approach: Hashmap

# m = number of unique sums in `nums`
# Time: O(n * log n)
# Space: O(m)

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digit_sum_dict = {}
        max_sum = -1

        for num in nums:
            digit_sum = sum(int(digit) for digit in str(num))

            if digit_sum in digit_sum_dict:
                max_sum = max(max_sum, digit_sum_dict[digit_sum] + num)
                digit_sum_dict[digit_sum] = max(digit_sum_dict[digit_sum], num)
            else:
                digit_sum_dict[digit_sum] = num

        return max_sum
        
