class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        adj = {}
        for a,b in edges:
            if a not in adj:
                adj[a] = []
            if b not in adj:
                adj[b] = []
            
            adj[a].append(b)
            adj[b].append(a)

        seen = set()
        def helper(n):
            seen.add(n)
            if n not in adj:
                return 

            for node in adj[n]:
                if node not in seen:
                    helper(node)
        
        helper(0)
        return len(seen) == n
