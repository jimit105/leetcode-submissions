# Approach 1: Dijkstra's Algorithm

# e = total no. of edges
# Time: O((n + e) log n)
# Space: O(n + e)

import heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7

        graph = [[] for _ in range(n)]

        for start_node, end_node, travel_time in roads:
            graph[start_node].append((end_node, travel_time))
            graph[end_node].append((start_node, travel_time))

        min_heap = [(0, 0)] # (time, node)
        shortest_time = [float('inf')] * n
        path_count = [0] * n # No. of ways to reach node in shortest time

        shortest_time[0] = 0
        path_count[0] = 1

        while min_heap:
            curr_time, curr_node = heapq.heappop(min_heap)
            if curr_time > shortest_time[curr_node]:
                continue

            for neighbor_node, road_time in graph[curr_node]:
                # Found a new shortest path → Update shortest time and reset path count
                if curr_time + road_time < shortest_time[neighbor_node]:
                    shortest_time[neighbor_node] = curr_time + road_time
                    path_count[neighbor_node] = path_count[curr_node]
                    heapq.heappush(min_heap, (shortest_time[neighbor_node], neighbor_node))

                # Found another way with the same shortest time → Add to path count
                elif curr_time + road_time == shortest_time[neighbor_node]:
                    path_count[neighbor_node] = (path_count[neighbor_node] + path_count[curr_node]) % MOD

        return path_count[n - 1]

