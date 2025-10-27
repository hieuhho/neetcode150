# Merge Intervals
# Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# You may return the answer in any order.

# Note: Intervals are non-overlapping if they have no common point. For example, [1, 2] and [3, 4] are non-overlapping, but [1, 2] and [2, 3] are overlapping.

# Example 1:

# Input: intervals = [[1,3],[1,5],[6,7]]

# Output: [[1,5],[6,7]]
# Example 2:

# Input: intervals = [[1,2],[2,3]]

# Output: [[1,3]]
# Constraints:

# 1 <= intervals.length <= 1000
# intervals[i].length == 2
# 0 <= start <= end <= 1000

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ans = []
        n = len(intervals)
        i = 1
        ans.append(intervals[0])
        while i < n:
            start1, end1 = ans[-1]
            start2, end2 = intervals[i]

            if start2 <= end1:
                new_start = min(start1, start2)
                new_end = max(end1, end2)
                ans[-1] = [new_start, new_end]
            else:
                ans.append([start2, end2])
            i += 1
        return ans
