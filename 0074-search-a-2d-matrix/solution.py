# Approach 1 - Binary Search

# Time: O(log(mn)), Space: O(1)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        
        left, right = 0, m * n - 1
        
        while left <= right:
            pivot_idx = left + (right - left) // 2
            pivot_element = matrix[pivot_idx // n][pivot_idx % n]
            
            if target == pivot_element:
                return True
            elif target < pivot_element:
                right = pivot_idx - 1
            else:
                left = pivot_idx + 1
                
        return False
