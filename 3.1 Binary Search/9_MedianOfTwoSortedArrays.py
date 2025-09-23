# Median of Two Sorted Arrays

# You are given two integer arrays nums1 and nums2 of size m and n respectively, where each is sorted in ascending order. Return the median value among all elements of the two arrays.

# Your solution must run in O(log(m+n))O(log(m+n)) time.

# Example 1:

# Input: nums1 = [1,2], nums2 = [3]

# Output: 2.0

# Explanation: Among [1, 2, 3] the median is 2.

# Example 2:

# Input: nums1 = [1,3], nums2 = [2,4]

# Output: 2.5

# Explanation: Among [1, 2, 3, 4] the median is (2 + 3) / 2 = 2.5.

# Constraints:

#     nums1.length == m
#     nums2.length == n
#     0 <= m <= 1000
#     0 <= n <= 1000
#     -10^6 <= nums1[i], nums2[i] <= 10^6

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()

        merged_len = len(merged)
        if merged_len % 2 == 0:
            return (merged[merged_len // 2 - 1] + merged[merged_len // 2]) / 2.0
        return merged[merged_len // 2]

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)

        # Always do the binary search on the smaller array.
        # Why? Because the time complexity is O(log(min(l1, l2))).
        # If nums1 is longer, we swap them so nums1 is always the shorter one.
        if l1 > l2:
            return self.findMedianSortedArrays(nums2, nums1)

        max_len = l1 + l2                  # total elements across both arrays
        half_len = max_len // 2            # "halfway point" index across both arrays combined

        # We are going to binary search inside nums1
        # The search range is indices [0 .. l1-1]
        l = 0
        r = l1 - 1

        while True:
            # Partition nums1 at index i. Think of i as "the last index on the left side of nums1".
            i = (l + r) // 2

            # Partition nums2 so that left halves together hold half_len elements.
            # j is "the last index on the left side of nums2".
            # The -2 is because both i and j are treated as left indices, not counts.
            j = half_len - i - 2

            # Values just to the left/right of the partitions.
            # If the partition is empty on one side, use -inf/+inf as placeholders.
            nums1_left  = nums1[i]     if i >= 0 else float("-infinity")
            nums1_right = nums1[i + 1] if (i + 1) < l1 else float("infinity")
            nums2_left  = nums2[j]     if j >= 0 else float("-infinity")
            nums2_right = nums2[j + 1] if (j + 1) < l2 else float("infinity")

            # Check if we have a valid partition:
            #   - All left values <= all right values
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                # Case 1: odd total length
                # The median is simply the *first element on the right side*.
                if max_len % 2:
                    return min(nums1_right, nums2_right)
                # Case 2: even total length
                # The median is the average of the *largest left value* and the *smallest right value*.
                else:
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2

            # If the left side of nums1 is too large, move the partition left.
            elif nums1_left > nums2_right:
                r = i - 1
            # Otherwise, move the partition right.
            else:
                l = i + 1



