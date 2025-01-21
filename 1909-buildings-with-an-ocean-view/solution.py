# Approach 3: Monotonic Stack Space Optimization

# Time: O(n)
# Space: O(1)

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        answer = []
        max_height = -1

        for current in reversed(range(n)):
            if heights[current] > max_height:
                answer.append(current)
                max_height = heights[current]

        answer.reverse()
        return answer
        
