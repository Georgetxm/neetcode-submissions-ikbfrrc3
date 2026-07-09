class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        new_start, new_end = newInterval

        for idx, interval in enumerate(intervals):
            start, end = interval

            if new_end < start:
                res.append([new_start, new_end])
                return res + intervals[idx:]
            elif new_start > end:
                res.append(interval)
            else:
                new_start = min(new_start, start)
                new_end = max(new_end, end)

        res.append([new_start, new_end])

        return res

            


        