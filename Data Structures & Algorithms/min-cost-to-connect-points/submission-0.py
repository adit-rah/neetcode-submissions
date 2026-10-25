class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        res = 0
        visited = set() # index, since points are unique
        h = [(0,0)] # dist, index

        while len(visited) < n:
            dist, i = heapq.heappop(h)

            if i in visited:
                continue
            
            visited.add(i)
            res += dist
            ox,oy = points[i]

            for j in range(n):
                if j in visited:
                    continue
                
                x,y = points[j]

                new_dist = abs(ox-x) + abs(oy-y)
                heapq.heappush(h, (new_dist,j))
        
        return res
