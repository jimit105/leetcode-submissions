# https://youtu.be/fUa0LRtSlz0

import math

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        
        gcd = math.gcd(p, q)
        
        p /= gcd
        q /= gcd
        
        if q % 2 == 0:
            return 0
        
        elif p % 2 == 0:
            return 2
        
        else:
            return 1
        
