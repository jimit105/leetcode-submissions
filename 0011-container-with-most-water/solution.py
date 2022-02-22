# Approach 2 - Two Pointer Approach

# Time: O(n)
# Space: O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
        
        while l < r:
            max_area = max(max_area, min(height[r], height[l]) * (r - l))
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return max_area
        
