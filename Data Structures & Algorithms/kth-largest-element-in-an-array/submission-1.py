class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = [-e for e in nums]

        heapq.heapify(h)

        for _ in range(k-1):
            heapq.heappop(h)
        
        return -h[0]
