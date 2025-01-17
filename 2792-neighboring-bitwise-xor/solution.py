# Approach 2: Cumulative XOR

# Time: O(n)
# Space: O(1)

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        XOR = 0
        for element in derived:
            XOR ^= element
        
        return XOR == 0
        
