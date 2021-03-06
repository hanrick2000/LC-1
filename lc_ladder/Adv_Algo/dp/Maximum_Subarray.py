#! /usr/local/bin/python3

# https://www.lintcode.com/problem/maximum-subarray/description
# Example

"""
Algo: dp 滚动一维数组
D.S.:

Solution:
Time: O(n), Space: O(1)
DP 分析
1. 状态
f[i]: 以i为结尾的max sum 是多大
2. 方程
f[i] = max(f[i - 1] + nums[i], num[i])
3. 初始化
f[0] = nums[0]
4. 答案
max(f)
Corner cases:
"""

class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        if not nums:
            return 0
        res = nums[0]
        runner = nums[0]
        for i in range(1, len(nums)):
            runner = max(runner + nums[i], nums[i])
            res = max(res, runner)
        return res
# Test Cases
if __name__ == "__main__":
    solution = Solution()
