# Approach 2 - Categorize by count

# Time: O(n * k), n = length of strs, k = max lenth of string in strs
# Space: O(n * k)

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[(ord(c) - ord('a'))] += 1
            ans[tuple(count)].append(s)

        return list(ans.values())
        
