# Time: O(n)
# Space: O(n)

"""
Algorithm:
1. Convert the input number to a list of digits for easier manipulation.
2. Create a dictionary that stores the last position of each digit in the number.
3. For each position from left to right:
    a. Look for a larger digit (from 9 down to current digit) that appears later in the number
    b. If found, swap these digits and return the result
4. If no swap is needed (number is already maximum), return the original number.
"""

class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        n = len(digits)

        last_pos = {int(digit) : i for i, digit in enumerate(digits)}

        for i in range(n):
            current_digit = int(digits[i])

            for d in range(9, current_digit, -1):
                if d in last_pos and last_pos[d] > i:
                    digits[i], digits[last_pos[d]] = digits[last_pos[d]], digits[i]
                    return int(''.join(digits))

        return num

        
