# Approach: Sorting + Two Pointers + Greedy

# m = len(players), n = len(trainers)
# Time: O(m log m + n log n)
# Space: O(log m + log n)

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        m, n = len(players), len(trainers)
        i = j = count = 0

        while i < m and j < n:
            while j < n and players[i] > trainers[j]:
                j += 1
            if j < n:
                count += 1
            i += 1
            j += 1

        return count
        
