# Approach: Stack

# n = length of decoded string, m = number of nested brackets
# Time: O(n)
# Space: O(m)

class Solution:
    def decodeString(self, s: str) -> str:
        stack = [] # to keep track of nested brackets
        curr_str = ''
        curr_num = 0

        for char in s:
            if char.isdigit():
                # Build the number
                curr_num = curr_num * 10 + int(char)
            elif char == '[':
                # Push the curr num and str to stacj
                stack.append((curr_str, curr_num))
                # Reset current values
                curr_str = ''
                curr_num = 0
            elif char == ']':
                prev_str, num = stack.pop()
                curr_str = prev_str + curr_str * num
            else:
                # Add characters to the current str
                curr_str += char

        return curr_str
