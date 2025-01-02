# Approach 1: Merge Intervals

# M, N = lengths of `firstList` and `secondList` respectively
# Time: O(M + N)
# Space: O(M + N)

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        i = j = 0

        while i < len(firstList) and j < len(secondList):
            # Let's check if firstList[i] intersects secondList[j].
            # lo - the startpoint of the intersection
            # hi - the endpoint of the intersection
            lo = max(firstList[i][0], secondList[j][0])
            hi = min(firstList[i][1], secondList[j][1])
            if lo <= hi:
                ans.append([lo, hi])

            # Remove the interval with the smallest endpoint
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return ans
