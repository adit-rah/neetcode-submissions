class MedianFinder:

    def __init__(self):
       self.mins = []
       self.maxs = []

    def addNum(self, num: int) -> None:
        if not self.mins and not self.maxs:
            heapq.heappush(self.mins, -num)
            return
        
        if num < -self.mins[0]:
            heapq.heappush(self.mins, -num)
        else:
            heapq.heappush(self.maxs, num)

        if abs(len(self.mins) - len(self.maxs)) > 1:
            if len(self.mins) > len(self.maxs):
                heapq.heappush(self.maxs, -heapq.heappop(self.mins)) 
            else:
                heapq.heappush(self.mins, -heapq.heappop(self.maxs)) 


    def findMedian(self) -> float:
        if (len(self.mins) + len(self.maxs)) % 2 != 0:
            if len(self.mins) > len(self.maxs):
                return -self.mins[0]
            else:
                return self.maxs[0]
        else:
            return (-self.mins[0] + self.maxs[0]) / 2

        