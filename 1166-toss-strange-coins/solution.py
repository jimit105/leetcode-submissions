# Approach 1: Recursive Dynamic Programming

# Time: O(n * target)
# Space: O(n * target)

class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        memo = {}

        def find_probability(index, target, n):
            if target < 0:
                return 0

            if index == n:
                if target == 0:
                    return 1
                else:
                    return 0

            if (index, target) in memo:
                return memo[index, target]

            memo[index, target] = find_probability(index + 1, target - 1, n) * prob[index] + find_probability(index + 1, target, n) * (1 - prob[index])

            return memo[index, target]

        return find_probability(0, target, len(prob))

        
