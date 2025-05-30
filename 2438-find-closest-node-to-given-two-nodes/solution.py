# Approach 2: Depth First Search

# Time: O(n)
# Space: O(n)

class Solution:
    def dfs(self, node, edges, dist, visit):
        visit[node] = True
        neighbor = edges[node]
        if neighbor != -1 and not visit[neighbor]:
            dist[neighbor] = dist[node] + 1
            self.dfs(neighbor, edges, dist, visit)


    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        dist1 = [float('inf')] * n
        dist2 = [float('inf')] * n
        dist1[node1] = 0
        dist2[node2] = 0
        
        visit1 = [False] * n
        visit2 = [False] * n

        self.dfs(node1, edges, dist1, visit1)
        self.dfs(node2, edges, dist2, visit2)

        minDistNode = -1
        minDistTillNow = float('inf')

        for currNode in range(n):
            if minDistTillNow > max(dist1[currNode], dist2[currNode]):
                minDistNode = currNode
                minDistTillNow = max(dist1[currNode], dist2[currNode])

        return minDistNode
