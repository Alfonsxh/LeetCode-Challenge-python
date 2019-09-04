#
# @lc app=leetcode id=495 lang=python3
#
# [495] Teemo Attacking
#
from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0

        res = 0
        for i in range(len(timeSeries)):
            if i == 0:
                continue

            if timeSeries[i - 1] + duration >= timeSeries[i]:
                res += timeSeries[i] - timeSeries[i - 1]
            else:
                res += duration

        return res + duration


if __name__ == '__main__':
    print(Solution().findPoisonedDuration([1, 4], 2))
    print(Solution().findPoisonedDuration([1, 2], 2))
    print(Solution().findPoisonedDuration([1], 2))
