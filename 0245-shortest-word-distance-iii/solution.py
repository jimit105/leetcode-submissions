# Approach 3: Two Pointer

# Time: O(N)
# Space: O(1)

class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        shortest_distance = float('inf')
        prev_index = -1

        for i in range(len(wordsDict)):
            if wordsDict[i] in [word1, word2]:
                if prev_index != -1 and (wordsDict[prev_index] != wordsDict[i] or word1 == word2):
                    shortest_distance = min(shortest_distance, i - prev_index)

                prev_index = i

        return shortest_distance
