# Time: O(n)
# Space: O(n)

class Solution:
    def myAtoi(self, s: str) -> int:
        sign, result = 1, 0

        # Whitespace
        s = s.lstrip()

        if not s:
            return 0

        idx = 0

        # Signedness
        if s[idx] == '-':
            sign = -1
            idx += 1
        elif s[idx] == '+':
            idx += 1

        # Conversion
        int_str = ''
        for i in range(idx, len(s)):
            if s[i].isdigit():
                int_str += s[i]
            else:
                break

        result = sign * int(int_str) if int_str else 0

        # Rounding
        return max(min(result, 2 ** 31 - 1), -1 * 2 ** 31)

