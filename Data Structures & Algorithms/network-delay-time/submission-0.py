class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}

        for a,b,c in times:
            if a not in adj:
                adj[a] = [] 
            adj[a].append((b,c))
        
        h = [(0,k)]
        seen = set()
        t = 0
        while h:
            p1, n1 = heapq.heappop(h)
            if n1 in seen:
                continue
            
            seen.add(n1)
            t = max(t, p1)
            if n1 not in adj:
                continue 
            for other, plen in adj[n1]:
                heapq.heappush(h, (plen + p1, other))
            
        return t if len(seen) == n else -1

            

