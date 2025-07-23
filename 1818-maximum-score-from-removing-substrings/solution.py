# Approach 1: Greedy Way (Stack)

# Time: O(n)
# Space: O(n)

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        total_score = 0
        high_priority_pair = 'ab' if x > y else 'ba'
        low_priority_pair = 'ba' if high_priority_pair == 'ab' else 'ab'

        # First pass: Remove high_priority_pair
        string_after_first_pass = self.remove_substring(s, high_priority_pair)
        removed_pairs_count = (len(s) - len(string_after_first_pass)) // 2

        total_score += removed_pairs_count * max(x, y)

        # Second pass: Remove low_priority_pair
        string_after_second_pass = self.remove_substring(string_after_first_pass, low_priority_pair)
        removed_pairs_count = (len(string_after_first_pass) - len(string_after_second_pass)) // 2

        total_score += removed_pairs_count * min(x, y)

        return total_score

    def remove_substring(self, input, target_pair):
        char_stack = []

        for curr_char in input:
            if(
                curr_char == target_pair[1]
                and char_stack
                and char_stack[-1] == target_pair[0]
            ):
                char_stack.pop()
            else:
                char_stack.append(curr_char)

        return ''.join(char_stack)

        
