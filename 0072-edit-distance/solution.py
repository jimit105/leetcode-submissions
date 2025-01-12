# Approach 2: Memoization: Top-Down Dynamic Programming

# M = len(word1), N = len(word2)
# Time: O(M * N)
# Space: O(M * N)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = [
            [None for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)
        ]

        def minDistanceRecur(word1, word2, word1_idx, word2_idx):
            if word1_idx == 0:
                return word2_idx
            if word2_idx == 0:
                return word1_idx
            if memo[word1_idx][word2_idx] is not None:
                return memo[word1_idx][word2_idx]

            minEditDistance = 0
            if word1[word1_idx - 1] == word2[word2_idx - 1]:
                minEditDistance = minDistanceRecur(word1, word2, word1_idx - 1, word2_idx - 1)
            else:
                insert_operation = minDistanceRecur(word1, word2, word1_idx, word2_idx - 1)
                delete_operation = minDistanceRecur(word1, word2, word1_idx - 1, word2_idx)
                replace_operation = minDistanceRecur(word1, word2, word1_idx - 1, word2_idx - 1)
                minEditDistance = min(insert_operation, delete_operation, replace_operation) + 1

            memo[word1_idx][word2_idx] = minEditDistance
            return minEditDistance

        return minDistanceRecur(word1, word2, len(word1), len(word2))

