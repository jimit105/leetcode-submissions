# Approach: Sliding Window

# Time: O(n)
# Space: O(1)

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        curr_white = blocks[:k].count('W')

        min_operations = curr_white

        for i in range(k, len(blocks)):
            # Remove the contribution of the leftmost character
            if blocks[i - k] == 'W':
                curr_white -= 1

            if blocks[i] == 'W':
                curr_white += 1

            min_operations = min(min_operations, curr_white)

        return min_operations
        
