"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 70. Climbing Stairs.py
@time: 18-12-19 下午9:27
@version: v1.0
"""


class Solution(object):
    def rec_climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.rec_climbStairs(n - 1) + self.rec_climbStairs(n - 2)

    def dp_climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        a = 1
        b = 2
        for i in range(n - 2):
            tmp = a + b
            a = b
            b = tmp

        return b


if __name__ == '__main__':
    sol = Solution()
    print(sol.rec_climbStairs(23))
    print(sol.dp_climbStairs(23))
