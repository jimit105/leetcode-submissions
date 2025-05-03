# Approach: Greedy

# Time: O(n)
# Space: O(1)

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)

        def check(x):
            # Count rotations needed to make all tops x
            rotations_top = 0
            
            # Count rotations needed to make all bottoms x
            rotations_bottom = 0

            for i in range(n):
                # If neither top nor bottom is x, impossible
                if tops[i] != x and bottoms[i] != x:
                    return float('inf')
                # If top is not x but bottom is x
                elif tops[i] != x:
                    rotations_top += 1
                # If bottom is not x but top is x
                elif bottoms[i] != x:
                    rotations_bottom += 1

            return min(rotations_top, rotations_bottom)

        # Try making everything the value of first domino's bottom or first domino's bottom
        min_rotations = min(check(tops[0]), check(bottoms[0]))

        return -1 if min_rotations == float('inf') else min_rotations
