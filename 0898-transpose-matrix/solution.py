# Approach 1 - Copy Directly

# Time: O(R * C)
# Space: O(R * C)

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r, c = len(matrix), len(matrix[0])
        
        ans = [[None] * r for _ in range(c)]
        
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                ans[c][r] = val
        
        return ans
