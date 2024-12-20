# Time: O(n)
# Space: O(1)

class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        length = len(s)
        current_number = 0
        last_number = 0
        result = 0
        operation = '+'

        for i in range(length):
            current_char = s[i]

            if current_char.isdigit():
                current_number = (current_number * 10) + int(current_char)

            if (not current_char.isdigit() and not current_char.isspace()) or i == length - 1:
                if operation in ['+', '-']:
                    result += last_number
                    last_number = current_number if operation == '+' else -current_number
                elif operation == '*':
                    last_number = last_number * current_number
                elif operation == '/':
                    last_number = int(last_number / current_number)

                operation = current_char
                current_number = 0
        
        result += last_number
        return result
