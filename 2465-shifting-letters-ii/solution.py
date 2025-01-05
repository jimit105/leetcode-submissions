# Approach: Cumulative Shift

# n = length of shifts array, m = length of string
# Time: O(n + m)
# Space: O(m)

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        # Create array to track cumulative shifts for each position
        shift_count = [0] * n

        for start, end, direction in shifts:
            # Add 1 for forward shift, -1 for backward shift
            delta = 1 if direction == 1 else -1
            shift_count[start] += delta

            if end + 1 < n: # Cancel out effect after end position
                shift_count[end + 1] -= delta

        # Calculate prefix sum to get total shifts for each position
        for i in range(1, n):
            shift_count[i] += shift_count[i - 1]
        
        # Apply shifts all at once using modulo arithmetic
        result = []
        for i in range(n):
            # Calculate new character position
            new_pos = (ord(s[i]) - ord('a') + shift_count[i]) % 26
            result.append(chr(ord('a') + new_pos))

        return ''.join(result)
        
