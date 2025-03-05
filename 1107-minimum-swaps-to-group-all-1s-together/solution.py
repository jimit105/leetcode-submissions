# Approach 1: Sliding Window with Two Pointers

# Time: O(n)
# Space: O(1)

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = sum(data)
        count_ones = max_ones = 0
        left = right = 0

        while right < len(data):
            # updating the number of 1's by adding the new element
            count_ones += data[right]
            right += 1

            # maintain the length of the window to ones
            if right - left > ones:
                # Remove oldest element
                count_ones -= data[left]
                left += 1

            max_ones = max(max_ones, count_ones)

        return ones - max_ones

        
