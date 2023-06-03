from functools import lru_cache

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        @lru_cache(maxsize=None)
        def get_notification_time(i):
            if (manager[i]) != -1:
                return informTime[manager[i]] + get_notification_time(manager[i])
            else:
                return 0

        return max(get_notification_time(i) for i in range(n))
