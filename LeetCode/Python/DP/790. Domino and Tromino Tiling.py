"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 790. Domino and Tromino Tiling.py
@time: 18-12-20 下午8:00
@version: v1.0 
"""


class Solution(object):
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        # import numpy as np
        # dp = np.zeros((N + 1, 3), dtype=int)
        dp = [[0, 0, 0] for _ in range(N + 1)]
        dp[0][0] = 1
        dp[1][0] = 1

        for i in range(2, N + 1):
            dp[i][0] = dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2] + dp[i - 2][0]
            dp[i][1] = dp[i - 2][0] + dp[i - 1][2]
            dp[i][2] = dp[i - 2][0] + dp[i - 1][1]

        return dp[N][0] % (10 ** 9 + 7)


if __name__ == '__main__':
    sol = Solution()
    print(sol.numTilings(10))
