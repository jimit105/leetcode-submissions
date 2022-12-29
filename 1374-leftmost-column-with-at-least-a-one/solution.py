# Approach 2: Binary Search Each Row

# Time: O(N log M)
# Space: O(1)

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        smallest_index = cols

        for row in range(rows):
            lo = 0
            hi = cols - 1
            
            while lo < hi:
                mid = (lo + hi) // 2
                if binaryMatrix.get(row, mid) == 0:
                    lo = mid + 1
                else:
                    hi = mid

            if binaryMatrix.get(row, lo) == 1:
                smallest_index = min(smallest_index, lo)

        return -1 if smallest_index == cols else smallest_index
