# Approach 4: Floyd Warshall Algorithm

# n = number of courses (numCourses), q = len(queries)
# Time: O(n ^ 3 + q)
# Space: O(n ^ 2)

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        isPrerequisite = [[False] * numCourses for _ in range(numCourses)]

        for edge in prerequisites:
            isPrerequisite[edge[0]][edge[1]] = True

        for intermediate in range(numCourses):
            for src in range(numCourses):
                for target in range(numCourses):
                    isPrerequisite[src][target] = isPrerequisite[src][target] or (isPrerequisite[src][intermediate] and isPrerequisite[intermediate][target])

        answer = []
        for query in queries:
            answer.append(isPrerequisite[query[0]][query[1]])

        return answer
