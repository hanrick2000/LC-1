#! /usr/local/bin/python3

# https://www.lintcode.com/problem/word-ladder/description
# Example
# 给出两个单词（start和end）和一个字典，找到从start到end的最短转换序列
# 比如：
# 每次只能改变一个字母。
# 变换过程中的中间单词必须在字典中出现。
# 如果没有转换序列则返回0。
# 所有单词具有相同的长度。
# 所有单词都只包含小写字母。
#
# 样例
# 给出数据如下：
#
# start = "hit"
#
# end = "cog"
#
# dict = ["hot","dot","dog","lot","log"]
#
# 一个最短的变换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog"，
#
# 返回它的长度 5

"""
Algo: 经典BFS
D.S.:

Solution1:
超时
- 层级BFS数层数 模板
- 注意一些细节：end 应该先加在dict中
优化点在getPossibleVariations 每个数
共有M个词，每个数L长度
O(M * L * 26）
另外 nextWord in dict 是O(M) 因为是LIST 查询不是SET
Time: O(M * L * 26 * M）

Solution2:
用一个模糊查询词来存可能的变形
准备dict O(M * L * 26)
BFS O(M * L)
总共 Time: O(M * L) + O(M * L * 26)
Space: O(M * L) -- dict key number

Corner cases:
"""

class Solution1:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # write your code here
        if not start or not end or not dict:
            return 0
        from collections import deque

        # note that end may not in dict
        # only requirs middle steps in dict, so need to add end to dict
        dict.add(end)
        q = deque([start])
        visited = set([start])

        # 经典层级BFS 数层数的模板
        length = 0
        while len(q):
            length += 1
            for i in range(len(q)):
                curWord = q.popleft()
                if curWord == end:
                    return length
                for word in self.getPossibleVariations(curWord):
                    # 排除不在dict中的词
                    # 排除之前用过的词 hashset 在此题中的作用
                    if word not in dict or word in visited:
                        continue
                    q.append(word)
                    visited.add(word)
        return 0

    # O(26 * L)
    # L is the length of word
    def getPossibleVariations(self, word):
        chars = "abcdefghijklmnopqrstuvwxyz"
        ans = []
        for i in range(len(word)):
            for char in chars:
                if char == word[i]:
                    continue
                newWord = word[:i] + char + word[i + 1:]
                ans.append(newWord)
        return ans

class Solution_Optimal:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not beginWord or not endWord or not wordList:
            return 0

        # build wordMap
        # key: 'h*t' val: {'hit', 'hot'}
        wordMap = {}
        for word in wordList:
            for i in range(len(word)):
                vagueWord = word[:i] + '*' + word[i + 1 :]
                if vagueWord not in wordMap:
                    wordMap[vagueWord] = set()
                wordMap[vagueWord].add(word)

        # Prepare BFS 数层模板
        visited = set([beginWord])
        step = 0
        q = collections.deque([beginWord])

        while q:
            step += 1
            size = len(q)
            for _ in range(size):
                curWord = q.popleft()
                if curWord == endWord:
                    return step
                # 根据当前 的 模糊 字符 来选择下一个变形
                for i in range(len(curWord)):
                    vagueWord = curWord[:i] + '*' + curWord[i + 1 :]
                    if vagueWord in wordMap:
                        for word in wordMap[vagueWord]:
                            if word not in visited:
                                q.append(word)
                                visited.add(word)
        return 0
# Test Cases
if __name__ == "__main__":
    solution = Solution()
