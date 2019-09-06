#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        m, n = 0, len(matrix[0]) - 1
        while m < len(matrix) and n >= 0:
            tmp = matrix[m][n]
            if tmp == target:
                return True
            elif tmp < target:
                m += 1
            else:
                n -= 1

        return False


if __name__ == '__main__':
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]

    print(Solution().searchMatrix(matrix=matrix, target=3))
    print(Solution().searchMatrix(matrix=matrix, target=11))
    print(Solution().searchMatrix(matrix=matrix, target=13))

    matrix = [
        [1]
    ]
    print(Solution().searchMatrix(matrix=matrix, target=1))
