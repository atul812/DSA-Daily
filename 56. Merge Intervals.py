class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]

        for i in range(1, len(intervals)):
            last = result[-1]
            curr = intervals[i]
            last_end = last[-1]
            curr_start = curr[0]
            if curr_start <= last_end:
                result[-1][1] = max(last_end, curr[1])
            else:
                result.append(curr)

        return result
