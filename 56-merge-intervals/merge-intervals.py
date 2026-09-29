class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if len(intervals) <= 1:
            return intervals
        
        intervals.sort()
        result = []

        new_interval = intervals[0]
        result.append(new_interval)

        for interval in intervals:
            if interval[0] <= new_interval[1]:
                new_interval[1] = max(new_interval[1], interval[1])
            else:
                new_interval = interval
                result.append(new_interval)
        return result
