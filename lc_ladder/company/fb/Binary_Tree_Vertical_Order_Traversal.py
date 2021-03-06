#! /usr/local/bin/python3

# https://www.lintcode.com/problem/binary-tree-vertical-order-traversal/description
# https://leetcode.com/problems/binary-tree-vertical-order-traversal/
# Example
# 给定二叉树，返回其节点值的垂直遍历顺序。 (即逐列从上到下)。
# 如果两个节点在同一行和同一列中，则顺序应 从左到右。
#
# Example
# 样例1
#
# 输入： {3,9,20,#,#,15,7}
# 输出： [[9],[3,15],[20],[7]]
# 解释：
#    3
#   /\
#  /  \
#  9  20
#     /\
#    /  \
#   15   7
# 样例2
#
# 输入： {3,9,8,4,0,1,7}
# 输出：[[4],[9],[3,0,1],[8],[7]]
# 解释：
#      3
#     /\
#    /  \
#    9   8
#   /\  /\
#  /  \/  \
#  4  01   7

"""
Algo: BFS + map
D.S.: binary tree

Solution:
纵向的level巧妙记录
注意 Leetcode 的特殊要求
     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  21   7
 返回  [[4],[9],[3,1,2],[8],[7]]
3， 2， 1位于同一层，
3 在最上面
2，1 在同一层，虽然2 在1左边出现，但是1 更小，所以返回3， 1， 2
见下 Solution3_BFS_Leetcode 解法

Corner cases:
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution1_BFS:
    """
    @param root: the root of tree
    @return: the vertical order traversal
    """
    def verticalOrder(self, root):
        # write your code here
        from collections import deque
        if not root:
            return []
        res = []
        q = deque([(root, 0)])
        level_map = {0: [root.val]}
        while q:
            (cur_node, level) = q.popleft()
            if cur_node.left:
                q.append((cur_node.left, level - 1))
                if level - 1 not in level_map:
                    level_map[level - 1] = []
                level_map[level - 1].append(cur_node.left.val)
            if cur_node.right:
                q.append((cur_node.right, level + 1))
                if level + 1 not in level_map:
                    level_map[level + 1] = []
                level_map[level + 1].append(cur_node.right.val)

        print(level_map)
        for key in sorted(level_map):
            res.append(level_map[key])
        print(res)
        return res

class Solution2_BFS_No_Sorting:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        level_map = {} # key: level, val: [node.val]
        q = collections.deque([(root, 0)])
        minlevel, maxlevel = 0, 0
        while q:
            cur_node, level = q.popleft()
            minlevel = min(minlevel, level)
            maxlevel = max(maxlevel, level)

            if level not in level_map:
                level_map[level] = []
            level_map[level].append(cur_node.val)

            if cur_node.left:
                q.append((cur_node.left, level - 1))
            if cur_node.right:
                q.append((cur_node.right, level + 1))

        res = []
        for level in range(minlevel, maxlevel + 1):
            res.append(level_map[level])
        return res


class Solution3_BFS_Leetcode:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        level_map = {} # key: vertical level, val: [node val]
        lower, upper = 0, 0
        q = collections.deque([(root, 0)])
        while q:
            size = len(q)
            tmp_map = {}
            for _ in range(size):
                node, level = q.popleft()
                lower = min(lower, level)
                upper = max(upper, level)

                if level not in tmp_map:
                    tmp_map[level] = []
                tmp_map[level].append(node.val)
                if node.left:
                    q.append((node.left, level - 1))
                if node.right:
                    q.append((node.right, level + 1))
            # from tmp_map to level_mp
            for level, arr in tmp_map.items():
                if level not in level_map:
                    level_map[level] = sorted(arr)
                else:
                    level_map[level].extend(sorted(arr))
        res = []
        for i in range(lower, upper + 1):
            res.append(level_map[i])
        return res


class Solution4_DFS:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []

        level_map = {} # key: level, val: [node.val]
        boundry = [0, 0]
        self.dfs(root, 0, 0, level_map, boundry)

        res = []
        for level in range(boundry[0], boundry[1] + 1):
            # 根据题意 要根据行来排序
            level_map[level].sort(key=lambda x: x[0])
            res.append([x[1] for x in level_map[level]])
        return res

    def dfs(self, node, row, level, level_map, boundry):
        if not node: return

        low, high = boundry[0], boundry[1]
        boundry[0] = min(low, level)
        boundry[1] = max(high, level)

        if level not in level_map:
            level_map[level] = []
        level_map[level].append((row, node.val))
        self.dfs(node.left, row + 1, level - 1, level_map, boundry)
        self.dfs(node.right, row + 1, level + 1, level_map, boundry)

# Test Cases
if __name__ == "__main__":
    solution = Solution()
