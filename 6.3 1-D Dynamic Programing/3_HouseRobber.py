# House Robber

# You are given an integer array nums where nums[i] represents the amount of money the ith house has. The houses are arranged in a straight line, i.e. the ith house is the neighbor of the (i-1)th and (i+1)th house.

# You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.

# Return the maximum amount of money you can rob without alerting the police.

# Example 1:

# Input: nums = [1,1,3,3]

# Output: 4

# Explanation: nums[0] + nums[2] = 1 + 3 = 4.

# Example 2:

# Input: nums = [2,9,8,3,6]

# Output: 16

# Explanation: nums[0] + nums[2] + nums[4] = 2 + 8 + 6 = 16.

# Constraints:

#     1 <= nums.length <= 100
#     0 <= nums[i] <= 100
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        # create answer arr
        ans = [0] * len(nums)
        # set first 2 steps
        ans[0] = nums[0]
        ans[1] = max(nums[0], nums[1])

        # we set i as the maximum amount
        # since we cannot rob adjacent house, the max is either i + (i - 2) or just i
        for i in range(2, len(nums)):
            ans[i] = max(ans[i - 1], nums[i] + ans[i - 2])      # ans[i - 1] = skip
                                                                # nums[i] + ans[i-2] = rob this house (so skip the previous one)
        # last i is the largest amount
        return ans[-1]


# save memory
class Solution:
    def rob(self, nums: List[int]) -> int:
        start_1, start_2 = 0, 0
        for num in nums:
            temp = max(start_1 + num, start_2)
            start_1 = start_2
            start_2 = temp
        return start_2