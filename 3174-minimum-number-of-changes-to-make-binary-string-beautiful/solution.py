# Approach 1: Greedy

# Time: O(n)
# Space: O(1)

class Solution:
    def minChanges(self, s: str) -> int:
        current_char = s[0]

        consecutive_count = 0
        min_changes_reqd = 0

        for char in s:
            # If current char matches the prev sequence
            if char == current_char:
                consecutive_count += 1
                continue

                # If we have even count of chars, start a new seq
            if consecutive_count % 2 == 0:
                consecutive_count = 1
            
            # If odd count, change the current char
            else:
                consecutive_count = 0
                min_changes_reqd += 1

            # Update current char for next iteration
            current_char = char

        return min_changes_reqd

