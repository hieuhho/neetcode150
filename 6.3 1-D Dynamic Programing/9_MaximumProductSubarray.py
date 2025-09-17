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
        # final answer initialized as the largest single element (handles negatives/zeros)
        ans = max(nums)

        # current_max = max product ending at current index
        # current_min = min product ending at current index (important for negatives)
        current_max, current_min = 1, 1

        for n in nums:
            # store current_max before updating, because current_min update needs the old value
            tmp_max = current_max

            # update the maximum product at this index
            # three cases:
            # 1. extend previous max product with n
            # 2. extend previous min product with n (if n is negative, min*negative → max)
            # 3. start fresh from n
            current_max = max(n * current_max, n * current_min, n)

            # update the minimum product at this index (mirror logic of above)
            current_min = min(n * tmp_max, n * current_min, n)

            # track the overall maximum seen so far
            ans = max(ans, current_max, current_min)

        return ans