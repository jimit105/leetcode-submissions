# Approach: Greedy

# Time: O(n)
# Space: O(log n)

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for asteroid in asteroids:
            if mass < asteroid:
                return False
            mass += asteroid

        return True
        
