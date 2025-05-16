# Approach: Dynamic Programming

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(groups)
        dp = [1] * n
        prev = [-1] * n
        max_idx = 0

        for i in range(1, n):
            for j in range(i):
                if(
                    self.check(words[i], words[j])
                    and dp[j] + 1 > dp[i]
                    and groups[i] != groups[j]
                ):
                    dp[i] = dp[j] + 1
                    prev[i] = j

            if dp[i] > dp[max_idx]:
                max_idx = i

        ans = []
        i = max_idx

        while i >= 0:
            ans.append(words[i])
            i = prev[i]
        ans.reverse()
        return ans

    def check(self, s1, s2):
        if len(s1) != len(s2):
            return False
        diff = 0
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                diff += 1
                if diff > 1:
                    return False

        return diff == 1
        
