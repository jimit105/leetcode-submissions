# Approach 1: Top-down Dynamic Programming

# Time: O(n * amount)
# Space: O(n * amount)

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def number_of_ways(i, amount):
            if amount == 0:
                return 1
            if i == len(coins):
                return 0
            if memo[i][amount] != -1:
                return memo[i][amount]

            if coins[i] > amount:
                memo[i][amount] = number_of_ways(i + 1, amount)
            else:
                memo[i][amount] = number_of_ways(i, amount - coins[i]) + number_of_ways(i + 1, amount)

            return memo[i][amount]

        memo = [[-1] * (amount + 1) for _ in range(len(coins))]

        return number_of_ways(0, amount)
