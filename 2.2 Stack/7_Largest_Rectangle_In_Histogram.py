# Largest Rectangle In Histogram

# You are given an array of integers heights where heights[i] represents the height of a bar. The width of each bar is 1.

# Return the area of the largest rectangle that can be formed among the bars.

# Note: This chart is known as a histogram.

# Example 1:

# Input: heights = [7,1,7,2,2,4]

# Output: 8

# Example 2:

# Input: heights = [1,3,7]

# Output: 7

# Constraints:

#     1 <= heights.length <= 1000.
#     0 <= heights[i] <= 1000

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # make left and right stacks
        # first loop through list from left
        #   add the nearest smaller value to left[i]
        # loop through list from right
        #   add nearest smaller value to right[i]
        # loop through hieghts
        #   area = hiehgts[i] * (right[i] - left[i] - 1)
        # return largestArea
        n = len(heights)
        left_index, right_index = [-1] * n, [n] * n
        stack  = []
        largest_area = 0

        # find the smallest value index to the left of heights[i]
        for i in range(n):
            while stack and heights[stack [-1]] >= heights[i]:
                stack.pop()
            if stack:
                left_index[i] = stack[-1]
            stack.append(i)

        stack.clear()

        for i in range(n -1, -1, -1):
            while stack and heights[stack [-1]] >= heights[i]:
                stack.pop()
            if stack:
                right_index[i] = stack[-1]
            stack.append(i)

        for i in range(n):
            largest_area = max(largest_area, heights[i] * (right_index[i] - left_index[i] -1))
        return largest_area