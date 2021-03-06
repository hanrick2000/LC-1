#! /usr/local/bin/python3

# https://leetcode.com/problems/car-fleet/
# Example
# N cars are going to the same destination along a one lane road.  The destination is target miles away.
#
# Each car i has a constant speed speed[i] (in miles per hour), and initial position position[i] miles towards the target along the road.
#
# A car can never pass another car ahead of it, but it can catch up to it, and drive bumper to bumper at the same speed.
#
# The distance between these two cars is ignored - they are assumed to have the same position.
#
# A car fleet is some non-empty set of cars driving at the same position and same speed.  Note that a single car is also a car fleet.
#
# If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.
#
#
# How many car fleets will arrive at the destination?
#
#
#
# Example 1:
#
# Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
# Output: 3
# Explanation:
# The cars starting at 10 and 8 become a fleet, meeting each other at 12.
# The car starting at 0 doesn't catch up to any other car, so it is a fleet by itself.
# The cars starting at 5 and 3 become a fleet, meeting each other at 6.
# Note that no other cars meet these fleets before the destination, so the answer is 3.
#
# Note:
#
# 0 <= N <= 10 ^ 4
# 0 < target <= 10 ^ 6
# 0 < speed[i] <= 10 ^ 6
# 0 <= position[i] < target
# All initial positions are different.
"""
Algo:
D.S.:

Solution:
Time: O(nlogn) -- sort


Corner cases:
"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not position or not speed:
            return 0
        time_list = []
        for i in range(len(position)):
            time_to_target = (target - position[i]) / speed[i]
            time_list.append([position[i], time_to_target])
        time_list = sorted(time_list, key=lambda x: x[0])
        print(time_list)
        res = len(position)
        pre_time = time_list[-1][1]
        for i in range(len(position) - 2, -1, -1):
            cur_pos, cur_time = time_list[i][0], time_list[i][1]
            if cur_time <= pre_time:
                # if can catch up with prev one
                res -= 1
            else:
                # if cannot catch up with prev one
                pre_time = cur_time
        return res

# Test Cases
if __name__ == "__main__":
    solution = Solution()
