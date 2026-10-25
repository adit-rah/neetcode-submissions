class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        intervals = deque(intervals)

        res = 0
        prev_s, prev_e = intervals.popleft()
        while intervals:
            curr_s, curr_e = intervals.popleft()

            if prev_e <= curr_s:
                prev_s, prev_e = curr_s, curr_e
                continue
            
            res += 1
            prev_e = min(prev_e, curr_e)
        
        return res 
