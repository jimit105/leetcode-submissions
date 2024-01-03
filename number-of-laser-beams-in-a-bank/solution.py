# Approach 1: Greedy

# Time: O(M * N), M = no. of strings, N = avg. length of strings
# Space: O(1)

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        lasers = 0
        prev = 0

        for row in bank:
            if nxt := row.count('1'):
                lasers += nxt * prev
                prev = nxt

        return lasers
        
