class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        curr = intervals[0]

        for start, end in intervals[1::]:
            merge_start, merge_end = curr

            if end < merge_start:
                res.append([start,end])
                continue
            
            if start > merge_end:
                res.append([merge_start, merge_end])
                curr = [start, end]
                continue
            
            curr = [
                min(merge_start, start),
                max(merge_end, end) 
            ]
        
        res.append(curr)
        return res