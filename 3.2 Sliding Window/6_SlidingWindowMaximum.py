# Sliding Window Maximum

# You are given an array of integers nums and an integer k. There is a sliding window of size k that starts at the left edge of the array. The window slides one position to the right until it reaches the right edge of the array.

# Return a list that contains the maximum element in the window at each step.

# Example 1:

# Input: nums = [1,2,1,0,4,2,6], k = 3

# Output: [2,2,4,4,6]

# Explanation:
# Window position            Max
# ---------------           -----
# [1  2  1] 0  4  2  6        2
#  1 [2  1  0] 4  2  6        2
#  1  2 [1  0  4] 2  6        4
#  1  2  1 [0  4  2] 6        4
#  1  2  1  0 [4  2  6]       6

# Constraints:

#     1 <= nums.length <= 1000
#     -10,000 <= nums[i] <= 10,000
#     1 <= k <= nums.length

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        q = deque()
        l = r = 0

        # keep the queue in decreasing order
        while r < len(nums):
            # pop smaller values
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # resize window, q[0] is always the largest but we have to resize due to k
            if q[0] < l:
                q.popleft()

            # when we have a valid k window, add q[0] then move l forward
            if (r + 1) >= k:
                ans.append(nums[q[0]])
                l += 1
            r += 1
        return ans