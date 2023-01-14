# Approach 1: Greedy

# Time: O(n)
# Space: O(1)

class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        max_damage = 0
        total_damage = 0

        for d in damage:
            total_damage += d
            max_damage = max(max_damage, d)

        return total_damage - min(armor, max_damage) + 1
