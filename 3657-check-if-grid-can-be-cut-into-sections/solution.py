# Approach: Line Sweep

# Time: O(n log n)
# Space: O(n)

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        # Check if valid cuts can be made in a specific dimension
        def _check_cuts(rectangles, dim):
            gap_count = 0
            rectangles.sort(key=lambda rect: rect[dim])

            furthest_end = rectangles[0][dim + 2]
            
            for i in range(1, len(rectangles)):
                rect = rectangles[i]
                if furthest_end <= rect[dim]:
                    gap_count += 1

                furthest_end = max(furthest_end, rect[dim + 2])

            return gap_count >= 2

        return _check_cuts(rectangles, 0) or _check_cuts(rectangles, 1)

        
