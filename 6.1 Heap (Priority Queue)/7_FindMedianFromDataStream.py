# Find Median From Data Stream

# The median is the middle value in a sorted list of integers. For lists of even length, there is no middle value, so the median is the mean of the two middle values.

# For example:

#     For arr = [1,2,3], the median is 2.
#     For arr = [1,2], the median is (1 + 2) / 2 = 1.5

# Implement the MedianFinder class:

#     MedianFinder() initializes the MedianFinder object.
#     void addNum(int num) adds the integer num from the data stream to the data structure.
#     double findMedian() returns the median of all elements so far.

# Example 1:

# Input:
# ["MedianFinder", "addNum", "1", "findMedian", "addNum", "3" "findMedian", "addNum", "2", "findMedian"]

# Output:
# [null, null, 1.0, null, 2.0, null, 2.0]

# Explanation:
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.findMedian(); // return 1.0
# medianFinder.addNum(3);    // arr = [1, 3]
# medianFinder.findMedian(); // return 2.0
# medianFinder.addNum(2);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0

# Constraints:

#     -100,000 <= num <= 100,000
#     findMedian will only be called after adding at least one integer to the data structure.

import heapq

class MedianFinder:

    def __init__(self):
        self.left_half = []       # max heap, stores min -> mid | use neg num so [0]
        self.right_half = []       # min heap stores mid -> max | use mid

    def addNum(self, num: int) -> None:
        middle = self.right_half[0] if self.right_half else float("inf")
        if middle < num:
            heapq.heappush(self.right_half, num)
        else:
            heapq.heappush(self.left_half, -num)

        if len(self.left_half) > len(self.right_half)  + 1:
            # "left is longer"
            heapq.heappush(self.right_half, -heapq.heappop(self.left_half))
        elif len(self.right_half) > len(self.left_half)  + 1:
            # "right is longer"
            heapq.heappush(self.left_half, -heapq.heappop(self.right_half))


    def findMedian(self) -> float:
        len_diff = len(self.left_half) - len(self.right_half)

        if len(self.left_half) > len(self.right_half):
            return -self.left_half[0]
        if len(self.right_half) > len(self.left_half):
            return self.right_half[0]
        return (-self.left_half[0] + self.right_half[0]) / 2

