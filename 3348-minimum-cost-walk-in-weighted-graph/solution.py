# Approach 1: Disjoint-Set (Union-Find)

# m = len(edges), q = len(query)
# Time: O(m + q)
# Space: O(n)

from collections import deque

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        # Create adjacency list
        adj_list = [[] for _ in range(n)]
        for edge in edges:
            adj_list[edge[0]].append((edge[1], edge[2]))
            adj_list[edge[1]].append((edge[0], edge[2]))

        visited = [False] * n

        # Store component id of each node
        components = [0] * n
        component_cost = []
        component_id = 0
        
        # Perform BFS for each unvisited node to identify components and calculate their costs
        for node in range(n):
            if not visited[node]:
                component_cost.append(self._get_component_cost(node, adj_list, visited, components, component_id))
                component_id += 1

        result = []
        for q in query:
            start, end = q

            if components[start] == components[end]:
                # In same component
                result.append(component_cost[components[start]])
            else:
                # In different components
                result.append(-1)

        return result

    def _get_component_cost(self, source, adj_list, visited, components, component_id):
        nodes_queue = deque()

        component_cost = -1
        nodes_queue.append(source)
        visited[source] = True

        # Perform BFS to explore component and compute cost
        while nodes_queue:
            node = nodes_queue.popleft()

            components[node] = component_id

            for neighbor, weight in adj_list[node]:
                component_cost &= weight
                if visited[neighbor]:
                    continue
                visited[neighbor] = True
                nodes_queue.append(neighbor)

        return component_cost

