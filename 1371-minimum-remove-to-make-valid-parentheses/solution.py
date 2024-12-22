# Approach 1: Using Stack and String Builder

# Time: O(n)
# Space: O(n)

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        indices_to_remove = set()
        stack = [] # tracks the index

        for i, c in enumerate(s):
            if c not in "()":
                continue
            elif c == '(':
                stack.append(i)
            elif not stack:
                indices_to_remove.add(i)
            elif c == ')':
                stack.pop()

        indices_to_remove = indices_to_remove.union(set(stack))

        string_builder = []
        for i, c in enumerate(s):
            if i not in indices_to_remove:
                string_builder.append(c)

        return ''.join(string_builder)

