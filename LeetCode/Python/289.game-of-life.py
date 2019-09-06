#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if not m:
            return
        n = len(board[0])

        # 给board外层套一个框，方便计算周边存活的细胞数
        new_board = [[0 for _ in range(n + 2)]]
        [new_board.append([0] + line + [0]) for line in board]
        new_board.append([0 for _ in range(n + 2)])

        m, n = m + 1, n + 1

        for i in range(1, m):
            for j in range(1, n):
                life_num = self.__neighbor_life_num(new_board, i, j)
                if life_num < 2:
                    board[i - 1][j - 1] = 0

                if life_num > 3:
                    board[i - 1][j - 1] = 0

                if life_num == 3:
                    board[i - 1][j - 1] = 1

    def __neighbor_life_num(self, board, m, n):
        """计算周边存活的细胞数量"""
        is_alife = lambda a: 1 if a == 1 else 0

        return is_alife(board[m - 1][n - 1]) + is_alife(board[m - 1][n]) + is_alife(board[m - 1][n + 1]) \
               + is_alife(board[m][n - 1]) + is_alife(board[m][n + 1]) \
               + is_alife(board[m + 1][n - 1]) + is_alife(board[m + 1][n]) + is_alife(board[m + 1][n + 1])


if __name__ == '__main__':
    board = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ]

    Solution().gameOfLife(board)
    print(board)
