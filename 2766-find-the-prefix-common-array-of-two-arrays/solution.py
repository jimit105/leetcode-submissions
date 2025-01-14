# Approach 3: Single Pass with Frequency Array

# Time: O(n)
# Space: O(n)

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        prefix_common_array = [0 for _ in range(n)]
        freq = [0 for _ in range(n + 1)]
        common_count = 0

        for current_idx in range(n):
            freq[A[current_idx]] += 1
            if freq[A[current_idx]] == 2:
                common_count += 1

            freq[B[current_idx]] += 1
            if freq[B[current_idx]] == 2:
                common_count += 1

            prefix_common_array[current_idx] = common_count

        return prefix_common_array
