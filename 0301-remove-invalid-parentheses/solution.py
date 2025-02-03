# Approach: Backtracking

# Time: O(2^n)
# Space: O(n)

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(s):
            count = 0
            for char in s:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                if count < 0:
                    return False
            return count == 0

        # Use backtracking to try different combinations of removals
        def backtrack(s, start, left_count, right_count):
            if left_count == 0 and right_count == 0:
                if isValid(s):
                    result.add(s)
                return

            for i in range(start, len(s)):
                # Skip duplicates (Optimization)
                if i > start and s[i] == s[i - 1]:
                    continue

                # Try removing left parenthesis
                if left_count > 0 and s[i] == '(':
                    backtrack(s[:i] + s[i+1 :], i, left_count - 1, right_count)

                # Try removing right parenthesis
                if right_count > 0 and s[i] == ')':
                    backtrack(s[:i] + s[i+1 :], i, left_count, right_count - 1)

        # Count invalid parentheses
        left = right = 0
        for char in s:
            if char == '(':
                left += 1
            elif char == ')':
                if left == 0:
                    right += 1
                else:
                    left -= 1

        result = set()
        backtrack(s, 0, left, right)
        return list(result)

