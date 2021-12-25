from collections import defaultdict
class Solution:
    WHITE = 1 # not visited
    GRAY = 2 # ongoing vertex
    BLACK = 3 # visited
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        
        for src, dest in prerequisites:
            adj_list[src].append(dest)
            
        topo_order = []
        is_possible = True
        
        color = {k: Solution.WHITE for k in range(numCourses)}
        
        def dfs(node):
            nonlocal is_possible
            
            if not is_possible:
                return
            
            # mark node as ongoing
            color[node] = Solution.GRAY
            
            if node in adj_list:
                for neighbor in adj_list[node]:
                    if color[neighbor] == Solution.WHITE:
                        dfs(neighbor)
                        
                    # If there is another node with GRAY, then it means there is a cycle
                    elif color[neighbor] == Solution.GRAY:
                        is_possible = False
                        
            color[node] = Solution.BLACK
            topo_order.append(node)
            
        for vertex in range(numCourses):
            if color[vertex] == Solution.WHITE:
                dfs(vertex)
                
        return topo_order[:] if is_possible else []
        
        
        
