# Approach 1: Backtracking

# Time: O(n * 4^n)

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        answers = []

        def recurse(index, prev_operand, curr_operand, value, string):
            if index == n:
                # If the final value == target expected AND
                # no operand is left unprocessed
                if value == target and curr_operand == 0:
                    answers.append(''.join(string[1:]))
                return

            # Extending the current operand by one digit
            curr_operand = curr_operand * 10 + int(num[index])
            str_op = str(curr_operand)

            # To avoid cases where we have 1 + 05 or 1 * 05 
            if curr_operand > 0:
                # NO OP Recursion
                recurse(index + 1, prev_operand, curr_operand, value, string)

            # Addition
            string.append('+')
            string.append(str_op)
            recurse(index + 1, curr_operand, 0, value + curr_operand, string)
            string.pop()
            string.pop()

            # Can substract or multiply only if there are some previous operands
            if string:
                # Subtraction
                string.append('-')
                string.append(str_op)
                recurse(index + 1, -curr_operand, 0, value - curr_operand, string)
                string.pop()
                string.pop()

                # Multiplication
                string.append('*')
                string.append(str_op)
                recurse(index + 1, curr_operand * prev_operand, 0, value - prev_operand + (curr_operand * prev_operand), string)
                string.pop()
                string.pop()

        recurse(0, 0, 0, 0, [])
        return answers

