class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []

        for a,b in points:
            dist = math.sqrt(a**2 + b**2)

            heapq.heappush(h, [dist, a, b])
        
        res = []
        for i in range(k):
            e = heapq.heappop(h)
            res.append([e[1],e[2]])
        
        return res