"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key=lambda i: i.start)

        for i in range(1, len(intervals)):
            prev_interval = intervals[i - 1]
            cur_interval = intervals[i]

            if prev_interval.end > cur_interval.start:
                return False            

        return True

