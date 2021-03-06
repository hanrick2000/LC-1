#! /usr/local/bin/python3

# https://www.lintcode.com/problem/house-robber/description
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
# the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and
# it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house,
# determine the maximum amount of money you can rob tonight without alerting the police.
#
# Example
# Given [3, 8, 4], return 8.
#
# Challenge
# O(n) time and O(1) memory.

"""
Algo: DP
D.S.: Array 序列型dp

Solution:

Complexity: time: O(N), space: O(1)

DP 分析
1. 状态
f[i]: 前i个房子中，偷到的最大值
2. 方程
f[i] = max(f[i - 1], f[i - 2] + A[i - 1])
前i个最大值 = 1）前i-1的最大值，2）前i-2（偷i-2）的最大值加上A[i-1] （注意是A[i-1]而不是A[i] 因为有padding)
3. 初始化
f[0] = 0 # 前0个，ie 0
f[1] = A[0] # 前1个， ie A[0]
4. 答案
f[n]

Corner cases:
[9, 3, 1, 2] ->
[9, 9, 10, 11] -> 11
"""

class Solution1:
    """
    @param A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber(self, A):
        # write your code here
        if not A:
            return 0
        if len(A) == 1:
            return A[0]

        f = [max(A[0], 0), max(A[0], A[1])]
        for i in range(2, len(A)):
            f[i % 2] = max(f[(i - 1) % 2], f[(i - 2) % 2] + A[i])
        return f[(len(A) - 1) % 2]

class Solution2:
    """
    @param A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber(self, A):
        # write your code here
        if not A:
            return 0

        f = [0, 0] # 表示【上一个不拿的结果，上一个拿的结果】
        for i in A:
            yes = f[1] + i
            no = max(f)
            f = [yes, no]
        return max(f)
# Test Cases
if __name__ == "__main__":
    testCases = [
        [828,125,740,724,983,321,773,678,841,842,875]
    ]
    s1 = Solution1()
    s2 = Solution2()
    for t in testCases:
        s1.houseRobber(t)
        s2.houseRobber(t)
