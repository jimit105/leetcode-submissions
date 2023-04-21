# Approach: Knapsack

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        self.mod = 10 ** 9 + 7

        @lru_cache(None)
        def num_ways(i, n, minProfit):
            if i == len(group):
                return int(minProfit == 0)

            else:
                res = num_ways(i + 1, n, minProfit)
                if n >= group[i]:
                    res += num_ways(i + 1, n - group[i], max(minProfit - profit[i], 0))

            return res % self.mod

        return num_ways(0, n, minProfit)
