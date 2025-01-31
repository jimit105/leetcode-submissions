# Approach 1: Schoolbook Addition with Carry

# Time: O(n)
# Space: O(1)

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits

            # If current digit is 9, make it 0 and continue to next digit
            digits[i] = 0

        # If we're here, it means all digits were 9
        # Need to add a new digit 1 at the beginning
        return [1] + digits
        
