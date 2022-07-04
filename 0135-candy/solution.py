# Approach 2: Using two arrays
    
# Time: O(n)
# Space: O(n)

class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        total = 0
        n = len(ratings)
        left2right = [1] * n
        right2left = [1] * n
        
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left2right[i] = left2right[i - 1] + 1
                
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right2left[i] = right2left[i + 1] + 1
                
        for i in range(n):
            total += max(left2right[i], right2left[i])
            
        return total
            
        
