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
        self.small = []         # max heap, stores min -> mid | use neg num so [0]
        self.large = []         # min heap, stores mid -> max | use mid


    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -num)

        if len(self.small) > len(self.large)  + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small)  + 1:
            heapq.heappush(self.small, -heapq.heappop(self.large))


    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-self.small[0] + self.large[0]) / 2


# this is slower but is more clear
class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        # always put in left
        heapq.heappush(self.left, -num)
        # move max(left) into right
        heapq.heappush(self.right, -heapq.heappop(self.left))
        # keep size ~=, left holds extra int if odd len
        if len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        # odd len, the median is on the left
        if len(self.left) > len(self.right):
            return -self.left[0]
        # even len,
        return (-self.left[0] + self.right[0]) / 2
