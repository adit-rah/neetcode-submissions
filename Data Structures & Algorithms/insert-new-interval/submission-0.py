class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []


        for start, end in intervals:
            ins_start, ins_end = newInterval
            if end < ins_start:
                res.append([start,end])
                continue
            
            if ins_end < start:
                res.append([ins_start,ins_end])
                newInterval = [start, end]
                continue
            
            newInterval = [
                min(ins_start, start),
                max(ins_end, end)
            ]
        
        res.append(newInterval)
        return res