#
# @lc app=leetcode id=1010 lang=python3
#
# [1010] Pairs of Songs With Total Durations Divisible by 60
#
from typing import List


class Solution:
    # def numPairsDivisibleBy60(self, time: List[int]) -> int:
    #     length = len(time)
    #
    #     res = 0
    #     for i in range(length):
    #         for j in range(i + 1, length):
    #             if (time[i] + time[j]) % 60 == 0:
    #                 res += 1
    #
    #     return res

    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        time_counter = [0 for i in range(60)]
        res = 0

        for t in time:
            # 下面两步的步骤不能乱
            res += time_counter[(60 - t % 60) % 60]
            time_counter[t % 60] += 1
        return res


if __name__ == '__main__':
    print(Solution().numPairsDivisibleBy60([30, 20, 150, 100, 40]))
    print(Solution().numPairsDivisibleBy60([60, 60, 60]))
