"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.start)
        last_in_room = [] # (s,e) for latest meeting in the room

        for curr in intervals:
            if last_in_room and last_in_room[0] <= curr.start:
                heapq.heappop(last_in_room)
            
            heapq.heappush(last_in_room, curr.end)
            
        
        return len(last_in_room)
