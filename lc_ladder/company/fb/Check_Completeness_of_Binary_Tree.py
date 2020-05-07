#! /usr/local/bin/python3

# https://leetcode.com/problems/check-completeness-of-a-binary-tree/
# Given a binary tree, determine if it is a complete binary tree.
#
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is completely filled,
# and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
#
# Example 1:
# Input: [1,2,3,4,5,6]
# Output: true
# Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}),
# and all nodes in the last level ({4, 5, 6}) are as far left as possible.
# Example 2:
# Input: [1,2,3,4,5,null,7]
# Output: false
# Explanation: The node with value 7 isn't as far left as possible.
"""
Algo: BFS
D.S.:

Solution:

Time: O(n) -- # of all nodes
Space: O(n)
Corner cases:
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root: return True
        node_list = [(root, 1)]
        i = 0
        while i < len(node_list):
            node, v = node_list[i]
            if node:
                node_list.append((node.left, v * 2))
                node_list.append((node.right, v * 2 + 1))
            i += 1
        return node_list[-1][1] == len(node_list)

# Test Cases
if __name__ == "__main__":
    solution = Solution()
