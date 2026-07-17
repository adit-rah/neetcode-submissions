class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            d[n] = 1 + d.get(n, 0)
        
        w = list(d.items())
        w.sort(key=lambda x: x[1])
        res = []
        for i in range(len(w)-1,len(w)-1-k,-1):
            res.append(w[i][0])
        return res