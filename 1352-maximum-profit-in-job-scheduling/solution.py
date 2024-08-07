# Approach: Dyanmic Programming

# https://leetcode.com/problems/maximum-profit-in-job-scheduling/discuss/2849538/EASY-TO-UNDERSTAND-COMMENTED-SOLUTION-IN-PYTHON
 
from bisect import bisect_left
    
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        
        n = len(startTime)
        dp = [0] * (n + 1)
        
        for i in reversed(range(n)):
            k = bisect_left(jobs, jobs[i][1], key=lambda j: j[0])
            dp[i] = max(jobs[i][2] + dp[k], dp[i + 1])
            
        return dp[0]
        
        
