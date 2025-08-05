# Car Fleet
# Solved

# There are n cars traveling to the same destination on a one-lane highway.

# You are given two arrays of integers position and speed, both of length n.

#     position[i] is the position of the ith car (in miles)
#     speed[i] is the speed of the ith car (in miles per hour)

# The destination is at position target miles.

# A car can not pass another car ahead of it. It can only catch up to another car and then drive at the same speed as the car ahead of it.

# A car fleet is a non-empty set of cars driving at the same position and same speed. A single car is also considered a car fleet.

# If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.

# Return the number of different car fleets that will arrive at the destination.

# Example 1:

# Input: target = 10, position = [1,4], speed = [3,2]

# Output: 1

# Explanation: The cars starting at 1 (speed 3) and 4 (speed 2) become a fleet, meeting each other at 10, the destination.

# Example 2:

# Input: target = 10, position = [4,1,0,7], speed = [2,2,1,1]

# Output: 3

# Explanation: The cars starting at 4 and 7 become a fleet at position 10. The cars starting at 1 and 0 never catch up to the car ahead of them. Thus, there are 3 car fleets that will arrive at the destination.

# Constraints:

#     n == position.length == speed.length.
#     1 <= n <= 1000
#     0 < target <= 1000
#     0 < speed[i] <= 100
#     0 <= position[i] < target
#     All the values of position are unique.

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # create hash of car position and speed
        # we have to sort the hash by positions in reverse order, as then we can know when the closest car arrives
            # this is because the closest car will always finish fist, if there is a faster car behind, it will join and become a fleet
        # find the arrive time of car when it finishes
        # if stack is empty (no arrive time in stack ans) add to ans
        # if arrive time greater than the last time in the ans, add to ans

        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        for pos, spd in cars:
            arrive_time = (target - pos) / spd
            if not stack or arrive_time > stack[-1]:
                stack.append(arrive_time)
        return len(stack)
