# Products of Array Except Self
# Solved

# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

# Each product is guaranteed to fit in a 32-bit integer.

# Follow-up: Could you solve it in O(n)O(n) time without using the division operation?

# Example 1:

# Input: nums = [1,2,4,6]

# Output: [48,24,12,8]

# Example 2:

# Input: nums = [-1,0,1,2,3]

# Output: [0,-6,0,0,0]

# Constraints:

#     2 <= nums.length <= 1000
#     -20 <= nums[i] <= 20

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        before = 1
        after = 1
        # First Pass: Build Prefix Product into ans
        for i in range(len(nums)):
            # At each index i, prefix contains the product of all elements before index i, so we:
            # Assign it to ans[i]
            ans[i] = before
            # Then multiply it by nums[i] for the next step
            before *= nums[i]
        for i in range(len(nums) -1, -1, -1):
            # postfix holds the product of all elements after i
            # So you multiply ans[i] *= postfix
            ans[i] *= after
            # update postfix for the next loop
            after *= nums[i]
        return ans

# why use this?
# reusing memory to minimize space and linear traversal with accumulation
# not allocating any extra array besides ans, which is required output anyway.
# only using:
#     prefix (1 int)
#     postfix (1 int)
# Thus, space complexity = O(1) extra space.

## first approach
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1] * n
        post = [1] * n
        ans = [1] * n
        for i in range(1, n):
            pre[i] = nums[i - 1] * pre[i - 1] 
        for i in range(n - 2, -1, -1):
            post[i] = nums[i + 1] * post[i + 1]
        print(pre)
        print(post)
        for i in range(n):
            ans[i] = pre[i] * post[i]
        return ans