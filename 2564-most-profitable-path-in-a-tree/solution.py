# Approach 1: Depth-First Search and Breadth-First Search

# Time: O(n)
# Space: O(n)

from collections import deque

class Solution:
    def __init__(self):
        self.bob_path = {}
        self.visited = []
        self.tree = []


    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)
        max_income = float('-inf')
        self.tree = [[] for _ in range(n)]
        self.bob_path = {}
        self.visited = [False] * n
        node_queue = deque([(0, 0, 0)])

        for edge in edges:
            self.tree[edge[0]].append(edge[1])
            self.tree[edge[1]].append(edge[0])
        
        self.find_bob_path(bob, 0)

        # BFS
        self.visited = [False] * n
        while node_queue:
            source_node, time, income = node_queue.popleft()

            # Alice reaches node first
            if source_node not in self.bob_path or time < self.bob_path[source_node]:
                income += amount[source_node]
            # Reach the node at the same time
            elif time == self.bob_path[source_node]:
                income += amount[source_node] // 2

            # Update max value if current node is a new leaf
            if len(self.tree[source_node]) == 1 and source_node != 0:
                max_income = max(max_income, income)

            # Explore adjacent unvisited vertices
            for adj_node in self.tree[source_node]:
                if not self.visited[adj_node]:
                    node_queue.append((adj_node, time + 1, income))

            # Mark and remove current node
            self.visited[source_node] = True

        return max_income

    # DFS
    def find_bob_path(self, source_node, time):
        self.bob_path[source_node] = time
        self.visited[source_node] = True

        if source_node == 0:
            return True

        for adj_node in self.tree[source_node]:
            if not self.visited[adj_node]:
                if self.find_bob_path(adj_node, time + 1):
                    return True

        # If node 0 isn't reached, remove current node from path
        self.bob_path.pop(source_node, None)
        return False
