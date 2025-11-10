# Partition Equal Subset Sum
# Solved

# You are given an array of positive integers nums.

# Return true if you can partition the array into two subsets, subset1 and subset2 where sum(subset1) == sum(subset2). Otherwise, return false.

# Example 1:

# Input: nums = [1,2,3,4]

# Output: true

# Explanation: The array can be partitioned as [1, 4] and [2, 3].

# Example 2:

# Input: nums = [1,2,3,4,5]

# Output: false

# Constraints:

#     1 <= nums.length <= 100
#     1 <= nums[i] <= 50

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # If the total sum is odd, it can't be split evenly into two subsets
        if sum(nums) % 2:
            return False

        # The target sum for each subset (half of total sum)
        target = sum(nums) // 2

        # dp[j] means: can we make a sum of 'j' using some of the numbers?
        dp = [False] * (target + 1)
        dp[0] = True  # Base case: a sum of 0 is always possible (by choosing nothing)

        # Iterate over each number in the array
        for num in nums:
            # Traverse backwards so each number is only used once per iteration
            for j in range(target, num - 1, -1):
                # If dp[j - num] is True, we can form j by adding 'num'
                dp[j] = dp[j] or dp[j - num]

        # If dp[target] is True, we can partition the array into two equal subsets
        return dp[target]

