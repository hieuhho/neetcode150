# Trapping Rain Water

# You are given an array of non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.

# Return the maximum area of water that can be trapped between the bars.

# Example 1:

# Input: height = [0,2,0,3,1,0,1,3,2,1]

# Output: 9

# Constraints:

#     1 <= height.length <= 1000
#     0 <= height[i] <= 1000

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans_arr = [0] * n
        current_max = 0
        left_max = [0] * n
        right_max = [0] * n

        current_max = 0
        for i in range(n):
            left_max[i] = current_max
            current_max = max(current_max, height[i])
        
        current_max = 0
        for i in range(n - 1, -1, -1):
            right_max[i] = current_max
            current_max = max(current_max, height[i])

        for i in range(n):
            water = min(left_max[i], right_max[i]) - height[i]
            ans_arr[i] = 0 if water < 0 else water
        return sum(ans_arr)