# Approach 1: Invert and Reverse

# Time: O(L), maximum number of digits in input number
# Space: O(L)

class Solution:
    def confusingNumber(self, n: int) -> bool:
        invert_map = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
            }

        rotated_number = []

        for ch in str(n):
            if ch not in invert_map:
                return False

            rotated_number.append(invert_map[ch])

        rotated_number = ''.join(rotated_number)

        return int(rotated_number[::-1]) != n
