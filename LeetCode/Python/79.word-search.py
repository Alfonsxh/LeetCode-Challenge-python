#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.visted = set()  # 记录已经检测过的点

        # 遍历整个字母表
        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.__search(word, i, j):
                    return True

        return False

    def __search(self, word, i, j):
        """从四个方向搜索word中的字母"""
        # word中没有剩余的字符，返回True，匹配成功
        if len(word) == 0:
            return True

        # 判断i，j是否越界，或者(i,j)是否已经检测过
        if i < 0 or i >= len(self.board) \
                or j < 0 or j >= len(self.board[i]) \
                or (i, j) in self.visted:
            return False

        # 如果(i,j)元素不是word中的首个字母，则没必要继续下去
        if self.board[i][j] != word[0]:
            return False

        # 检测过的点中添加当前的(i,j)
        self.visted.add((i, j))

        # 从四个方向，继续递归搜索word中的字符
        found = self.__search(word[1:], i - 1, j) \
                or self.__search(word[1:], i, j - 1) \
                or self.__search(word[1:], i + 1, j) \
                or self.__search(word[1:], i, j + 1)

        # 如果没有找到，则将(i,j)从检测过的点中删除
        if not found:
            self.visted.remove((i, j))

        return found


if __name__ == '__main__':
    word = "ABC"
    print(Solution().exist(board=[
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ], word=word))
