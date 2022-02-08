import math

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_end_right = values[0]
        res = -math.inf
        
        for i in range(1, len(values)):
            max_end_right = max(max_end_right, values[i - 1] + i - 1)
            res = max(res, max_end_right + values[i] - i)
            
        return res
        
        
