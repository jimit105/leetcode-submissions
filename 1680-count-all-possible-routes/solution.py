# Approach 1: Recursive Dynamic Programming

# Time: O(n^2 * fuel)
# Space: O(n * fuel)

class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)

        memo = {}
        
        def solve(curr_city, remaining_fuel):
            if remaining_fuel < 0:
                return 0
            if (curr_city, remaining_fuel) in memo:
                return memo[(curr_city, remaining_fuel)]

            ans = 0
            if curr_city == finish:
                ans = 1
            
            for next_city in range(n):
                if next_city != curr_city:
                    ans = (ans + solve(next_city, remaining_fuel - abs(locations[curr_city] - locations[next_city]))) % (10 ** 9 + 7)

            memo[(curr_city, remaining_fuel)] = ans
            return ans

        return solve(start, fuel)
