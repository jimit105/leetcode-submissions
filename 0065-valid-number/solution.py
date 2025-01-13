# Approach 1: Follow The Rules!

# Time: O(n)
# Space: O(1)

class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit = seen_exponent = seen_dot = False

        for i, c in enumerate(s):
            if c.isdigit():
                seen_digit = True
            elif c in ['+', '-']:
                if i > 0 and s[i - 1] not in ['e', 'E']:
                    return False
            elif c in ['e', 'E']:
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                seen_digit = False
            elif c == '.':
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True

            # Invalid character
            else:
                return False
        
        # Must have at least one number and number after 'e'/'E' if exists
        return seen_digit
        
