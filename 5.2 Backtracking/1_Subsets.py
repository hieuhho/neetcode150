# Subsets

# Given an array nums of unique integers, return all possible subsets of nums.

# The solution set must not contain duplicate subsets. You may return the solution in any order.

# Example 1:

# Input: nums = [1,2,3]

# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Example 2:

# Input: nums = [7]

# Output: [[],[7]]

# Constraints:

#     1 <= nums.length <= 10
#     -10 <= nums[i] <= 10

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                ans.append(subset.copy())
                return

            # include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # ignore nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return ans