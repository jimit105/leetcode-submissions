# Approach 2: Stack

# Time: O(n * m)
# Space: O(n + m)

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        part_length = len(part)

        for char in s:
            stack.append(char)

            if len(stack) >= part_length and self._check_match(stack, part, part_length):
                for _ in range(part_length):
                    stack.pop()

        return ''.join(stack)

    def _check_match(self, stack, part, part_length):
        return ''.join(stack[-part_length:]) == part
        
