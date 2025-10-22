# Task Scheduler

# You are given an array of CPU tasks tasks, where tasks[i] is an uppercase english character from A to Z. You are also given an integer n.

# Each CPU cycle allows the completion of a single task, and tasks may be completed in any order.

# The only constraint is that identical tasks must be separated by at least n CPU cycles, to cooldown the CPU.

# Return the minimum number of CPU cycles required to complete all tasks.

# Example 1:

# Input: tasks = ["X","X","Y","Y"], n = 2

# Output: 5

# Explanation: A possible sequence is: X -> Y -> idle -> X -> Y.

# Example 2:

# Input: tasks = ["A","A","A","B","C"], n = 3

# Output: 9

# Explanation: A possible sequence is: A -> B -> C -> Idle -> A -> Idle -> Idle -> Idle -> A.

# Constraints:

#     1 <= tasks.length <= 1000
#     0 <= n <= 100

import heapq
from collections import deque, Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count how many times each task appears
        count = Counter(tasks)

        # Python's heapq is a min-heap, so store negative counts
        # This way, the task with the *highest* remaining count is at heap[0]
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)

        time = 0
        q = deque()  # cooldown queue -> stores [remaining_count, ready_time]

        # Continue until all tasks are processed and cooldown queue is empty
        while max_heap or q:
            time += 1  # simulate one unit of CPU time

            # STEP 1: run a task if one is available
            if max_heap:
                # Pop task with largest remaining count (negative number)
                cnt = 1 + heapq.heappop(max_heap)   # Add 1 because cnt is negative
                if cnt:
                    # If still tasks of this type left, put it into cooldown
                    # ready_time = current time + n (when we can run it again)
                    q.append([cnt, time + n])

            # STEP 2: check if the earliest task in cooldown is ready again
            if q and q[0][1] == time:
                # Its cooldown expired, push it back into the heap
                heapq.heappush(max_heap, q.popleft()[0])

        # When heap and queue are empty, all tasks are done
        return time