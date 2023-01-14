# Approach 2: Union Find
# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/solutions/2867563/lexicographically-smallest-equivalent-string/comments/1756716

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        UF = {}

        def find(x):
            UF.setdefault(x, x)
            if x != UF[x]:
                UF[x] = find(UF[x])

            return UF[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x > root_y:
                UF[root_x] = root_y
            else:
                UF[root_y] = root_x

        for i in range(len(s1)):
            union(s1[i], s2[i])

        res = []
        for c in baseStr:
            res.append(find(c))

        return ''.join(res)
