"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 509. Fibonacci Number.py
@time: 2019/4/11 下午8:29
@version: v1.0 
"""


class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N

        a, b = 0, 1
        for i in range(N - 1):
            a, b = b, a + b
        return b


if __name__ == '__main__':
    s = Solution()
    print(s.fib(20))
