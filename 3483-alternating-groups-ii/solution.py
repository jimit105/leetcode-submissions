# Approach 1: Expanding the Array & Sliding Window

# Time: O(n + k)
# Space: O(k)

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        # Expand the array for cirular sequences
        for i in range(k - 1):
            colors.append(colors[i])

        length = len(colors)
        result = 0
        left, right = 0, 1

        while right < length:
            # Check if the current color is the same as the last one
            if colors[right] == colors[right - 1]:

                # Pattern breaks, reset window from the current position
                left = right
                right += 1
                continue

            right += 1

            if right - left < k:
                continue

            result += 1
            left += 1

        return result

        
