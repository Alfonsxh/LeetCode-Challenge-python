"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 7. Reverse Integer.py
@time: 19-1-9 下午10:38
@version: v1.0 
"""


class Solution:
    def reverse(self, x: int):
        """
        :type x: int
        :rtype: int
        """
        less = False
        if x < 0:
            x = 0 - x
            less = True

        num_list = list()
        while x != 0:
            num_list.append(x % 10)
            x = x // 10

        res = 0
        for i in num_list:
            res = res * 10 + i

        res = 0 - res if less else res
        if -2 ** 31 < res < 2 ** 31 - 1:
            return res
        else:
            return 0

    def reverse2(self, x: int):
        """
        :type x: int
        :rtype: int
        """
        less = False
        str_x = str(x)
        if str_x[0] == '-':
            less = True
            str_x = str_x[1:]

        str_x = "".join(reversed(str_x))
        res = 0 - int(str_x) if less else int(str_x)

        if -2 ** 31 < res < 2 ** 31 - 1:
            return res
        else:
            return 0


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(12345))
    print(s.reverse(-12345))
    print(s.reverse(0))
    print(s.reverse2(12345))
    print(s.reverse2(-12345))
    print(s.reverse2(0))
