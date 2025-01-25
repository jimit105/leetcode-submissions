# Approach 1: Topological Sort Using Kahn's Algorithm

# n = no. of coures, m = len(prerequistes)
# Time: O(m + n)
# Space: O(m + n)

from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for prereq in prerequisites:
            adj[prereq[1]].append(prereq[0])
            indegree[prereq[0]] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        nodesVisited = 0
        while queue:
            node = queue.popleft()
            nodesVisited += 1

            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return nodesVisited == numCourses
        
