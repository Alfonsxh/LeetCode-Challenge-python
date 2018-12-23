"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 801. Minimum Swaps To Make Sequences Increasing.py
@time: 18-12-20 下午11:11
@version: v1.0 
"""


class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        length = len(A)
        swap = [float("inf") for _ in range(length)]
        keep = [float("inf") for _ in range(length)]

        swap[0], keep[0] = 1, 0

        for i in range(1, length):
            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                swap[i] = swap[i - 1] + 1
                keep[i] = keep[i - 1]

            if A[i] > B[i - 1] and B[i] > A[i - 1]:
                swap[i] = min(swap[i], keep[i - 1] + 1)
                keep[i] = min(swap[i - 1], keep[i])

        return min(swap[length - 1], keep[length - 1])


if __name__ == '__main__':
    sol = Solution()
    print(sol.minSwap([1, 3, 5, 4], [1, 2, 3, 7]))
