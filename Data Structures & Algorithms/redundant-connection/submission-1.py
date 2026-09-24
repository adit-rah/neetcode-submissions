class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = {}

        def find(x):
            if x not in adj:
                adj[x] = x
            
            if x != adj[x]:
                adj[x] = find(adj[x])
            
            return adj[x]
        
        res = [-1,-1]
        for a,b in edges:
            pa,pb = find(a), find(b)

            if pa == pb:
                res = [a,b]
            adj[pb] = pa
        print(adj.items())
    
        
        return res