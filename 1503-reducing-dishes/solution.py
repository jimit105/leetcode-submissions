# Approach 3: Bottom-up Dynamic Programming (Space Optimized)

# Time: O(N^2)
# Space: O(N)

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()

        # Array to keep the result for the previous iteration
        prev = [0] * (len(satisfaction) + 2)

        for index in range(len(satisfaction) - 1, -1, -1):
            # Array to keep the result for the current iteration
            dp = [0] * (len(satisfaction) + 2)

            for time in range(1, len(satisfaction) + 1):
                # Maximum of two choices:
                # 1. Cook the dish at `index` with the time taken as `time` and move on to the next dish with time as time + 1.
                # 2. Skip the current dish and move on to the next dish at the same time.
                dp[time] = max(satisfaction[index] * time + prev[time + 1], prev[time])

            prev = dp

        return prev[1]
