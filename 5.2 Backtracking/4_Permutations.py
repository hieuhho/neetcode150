# Permutations
# Given an array nums of unique integers, return all the possible permutations. You may return the answer in any order.

# Example 1:

# Input: nums = [1,2,3]

# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:

# Input: nums = [7]

# Output: [[7]]
# Constraints:

# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, path):
            if i == len(nums):
                res.append(path.copy())
                return

            for idx in range(i, len(path)):
                nums[i], nums[idx] = nums[idx], nums[i]
                backtrack(i + 1, path)
                nums[idx], nums[i] = nums[i], nums[idx]
        backtrack(0, nums)
        return res