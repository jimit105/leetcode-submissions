# Approach 1 - Next Array

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        N = len(seats)
        left, right = [N] * N, [N] * N
        
        for i in range(N):
            if seats[i] == 1:
                left[i] = 0
            elif i > 0:
                left[i] = left[i-1] + 1
                
        for i in range(N-1, -1, -1):
            if seats[i] == 1:
                right[i] = 0
            elif i < N-1:
                right[i] = right[i+1] + 1
            
                
        return max(min(left[i], right[i]) for i, seat in enumerate(seats) if not seat)
        
        
