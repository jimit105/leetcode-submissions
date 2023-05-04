# Approach 3: Binary Search with Boolean Array

# Time: O(N^2)
# Space: O(N)

import bisect

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        N = len(senate)

        banned = [False] * N

        r_indices = [i for i in range(N) if senate[i] == 'R']
        d_indices = [i for i in range(N) if senate[i] == 'D']

        
        def ban(indices_array, start_at):
            temp = bisect.bisect_left(indices_array, start_at)

            if temp == len(indices_array):
                banned[indices_array.pop(0)] = True
            else:
                banned[indices_array.pop(temp)] = True


        turn = 0
        while r_indices and d_indices:
            if not banned[turn]:
                if senate[turn] == 'R':
                    ban(d_indices, turn)
                else:
                    ban(r_indices, turn)

            turn = (turn + 1) % N

        return 'Radiant' if d_indices == [] else 'Dire'
        
