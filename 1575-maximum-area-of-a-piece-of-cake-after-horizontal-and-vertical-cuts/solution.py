# Approach: Sort

# Time: O(N*logN + M*logM), N = length of horizontal cuts, M = length of vertical cuts
# Space: O(1)

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        
        # Sort the inputs
        horizontalCuts.sort()
        verticalCuts.sort()
        
        # Calculate the maxHeight
        maxHeight = max(horizontalCuts[0], h - horizontalCuts[-1]) # Edges
        for i in range(1, len(horizontalCuts)):
            # horizontalCuts[i] - horizontalCuts[i - 1] represents the distance between
            # two adjacent edges, and thus a possible height
            maxHeight = max(maxHeight, horizontalCuts[i] - horizontalCuts[i - 1])
            
            
        # Calculate the maxWidth
        maxWidth = max(verticalCuts[0], w - verticalCuts[-1]) # Edges
        # verticalCuts[i] - verticalCuts[i - 1] represents the distance between
            # two adjacent edges, and thus a possible width
        for i in range(1, len(verticalCuts)):
            maxWidth = max(maxWidth, verticalCuts[i] - verticalCuts[i - 1])
            
        return (maxHeight * maxWidth) % (10**9 + 7)
        
