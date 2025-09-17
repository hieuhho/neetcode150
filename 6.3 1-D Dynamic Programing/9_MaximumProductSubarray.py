# Maximum Product Subarray

# Given an integer array nums, find a subarray that has the largest product within the array and return it.

# A subarray is a contiguous non-empty sequence of elements within an array.

# You can assume the output will fit into a 32-bit integer.

# Example 1:

# Input: nums = [1,2,-3,4]

# Output: 4

# Example 2:

# Input: nums = [-2,-1]

# Output: 2

# Constraints:

#     1 <= nums.length <= 1000
#     -10 <= nums[i] <= 10

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
