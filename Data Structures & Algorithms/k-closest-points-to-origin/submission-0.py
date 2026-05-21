class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []

        for i,(a,b) in enumerate(points):
            res.append([math.sqrt(a**2 + b**2), i])

        res.sort(key=lambda x: x[0])

        result = []
        for i in range(0,k):
            result.append(points[res[i][1]])
        
        return result