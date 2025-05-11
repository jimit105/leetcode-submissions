# Approach 2: Counting

# Time: O(n)
# Space: O(1)

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cons_odds = 0

        for num in arr:
            if num % 2 == 1:
                cons_odds += 1
            else:
                cons_odds = 0

            if cons_odds == 3:
                return True

        return False
        
