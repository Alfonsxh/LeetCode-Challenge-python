#
# @lc app=leetcode id=873 lang=python3
#
# [873] Length of Longest Fibonacci Subsequence
#
from typing import List
from collections import defaultdict


class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        index_dict = {k: i for i, k in enumerate(A)}
        # 保存最长结果
        # 假设方程式为 c = a + b
        # 里面的键为 longest_dict[(a, c)] = longest 相对的最长距离
        longest_dict = defaultdict(lambda: 2)

        res = 0
        for c_index, c_value in enumerate(A):
            for a_index in range(c_index):
                # 查找符合的 b 索引号，没有则跳过
                b_index = index_dict.get(c_value - A[a_index], None)

                # 如果 b 存在，并且在 a 的前面
                # 则 longest_dict[(a, c)] = longest_dict[(b, a)] + 1
                # x, b, a, c
                # 其中可能是 x + b = a, b + a = c
                # 这里的意思就是 (a, c) 的最长距离 等于 (b, a) 的最长距离 +1
                if b_index is not None and b_index < a_index:
                    tmp = longest_dict[(a_index, c_index)] = longest_dict[(b_index, a_index)] + 1
                    res = max(res, tmp)

        return res if len(A) >= 3 else 0


if __name__ == '__main__':
    print(Solution().lenLongestFibSubseq([1, 2, 3, 4, 5, 6, 7, 8]))
    print(Solution().lenLongestFibSubseq([1, 3, 7, 11, 12, 14, 18]))
