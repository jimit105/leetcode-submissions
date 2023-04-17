# Time: O(n)
# Space: O(1)

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        result = []

        for i in range(len(candies)):
            result.append(candies[i] + extraCandies >= max_candies)

        return result
