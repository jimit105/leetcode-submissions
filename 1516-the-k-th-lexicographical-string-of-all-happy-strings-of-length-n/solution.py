# Approach 1: Backtracking

# Time: O(n * 2^n)
# Space: O(2^n)

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        current_str = ''
        happy_strings = []

        self.generate_happy_strings(n, current_str, happy_strings)

        if len(happy_strings) < k:
            return ''

        happy_strings.sort()
        return happy_strings[k - 1]

    def generate_happy_strings(self, n, current_str, happy_strings):
        if len(current_str) == n:
            happy_strings.append(current_str)
            return

        for current_char in ['a', 'b', 'c']:
            if len(current_str) > 0 and current_str[-1] == current_char:
                continue

            self.generate_happy_strings(n, current_str + current_char, happy_strings)
        
