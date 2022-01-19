class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        nums = set(range(1, n+1))
        
        def match(A):
            return all(nums == set(row) for row in A)
        
        return match(matrix) and match(zip(*matrix))
        
