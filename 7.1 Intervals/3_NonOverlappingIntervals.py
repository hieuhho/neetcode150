# Non-overlapping Intervals
# Given an array of intervals intervals where intervals[i] = [start_i, end_i], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

# Note: Intervals are non-overlapping even if they have a common point. For example, [1, 3] and [2, 4] are overlapping, but [1, 2] and [2, 3] are non-overlapping.

# Example 1:

# Input: intervals = [[1,2],[2,4],[1,4]]

# Output: 1
# Explanation: After [1,4] is removed, the rest of the intervals are non-overlapping.

# Example 2:

# Input: intervals = [[1,2],[2,4]]

# Output: 0
# Constraints:

# 1 <= intervals.length <= 1000
# intervals[i].length == 2
# -50000 <= starti < endi <= 50000

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        ans = 0
        intervals.sort(key=lambda x:x[0])
        prev_end = intervals[0][1]

        for s, e in intervals[1:]:
            if s >= prev_end:
                prev_end = e
            else:
                ans += 1
                prev_end = min(prev_end, e)

        return ans