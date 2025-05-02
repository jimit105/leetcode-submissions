# Approach 2: Calculate Force

# Time: O(N)

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        N = len(dominoes)
        force = [0] * N

        # Left to Right
        f = 0
        for i in range(N):
            if dominoes[i] == 'R':
                f = N
            elif dominoes[i] == 'L':
                f = 0
            else:
                f = max(f - 1, 0)
            force[i] += f

        # Right to Left
        f = 0
        for i in range(N - 1, -1, -1):
            if dominoes[i] == 'L':
                f = N
            elif dominoes[i] == 'R':
                f = 0
            else:
                f = max(f - 1, 0)
            force[i] -= f

        return ''.join('.' if f == 0 
                            else 'R' if f > 0 
                            else 'L'
                        for f in force)
