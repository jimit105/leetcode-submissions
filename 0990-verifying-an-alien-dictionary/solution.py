# Approach 1: Compare Adjacent Words

# Time: O(M), M = total no. of characters in `words`
# Space: O(1)

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {}
        for idx, val in enumerate(order):
            order_map[val] = idx

        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j >= len(words[i+1]):
                    return False

                if words[i][j] != words[i+1][j]:
                    if order_map[words[i][j]] > order_map[words[i+1][j]]:
                        return False

                    break

        return True
