# Approach 1 - Simulation + Heap

import heapq
import math

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        # heapq is min-heap
        # So use negative values to mimic max-heap
        evens = []
        minimum = math.inf
        
        for num in nums:
            if num % 2 == 0:
                evens.append(-num)
                minimum = min(minimum, num)
            else:
                evens.append(-num*2)
                minimum = min(minimum, num * 2)
                
        heapq.heapify(evens)
        
        min_deviation = math.inf
        while evens:
            current_val = -heapq.heappop(evens)
            min_deviation = min(min_deviation, current_val - minimum)
            
            if current_val % 2 == 0:
                minimum = min(minimum, current_val // 2)
                heapq.heappush(evens, -current_val // 2)
            else:
                # if the maximum is odd number, break
                break
                
        return min_deviation
        
        
        
