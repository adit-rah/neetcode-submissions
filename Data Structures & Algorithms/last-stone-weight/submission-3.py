class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        for val in stones:
            heapq.heappush(h, -val)
        
        while len(h) > 1:
            a = -heapq.heappop(h)
            b = -heapq.heappop(h)

            if a != b:
                heapq.heappush(h, -(a - b))

        return -h[0] if h else 0