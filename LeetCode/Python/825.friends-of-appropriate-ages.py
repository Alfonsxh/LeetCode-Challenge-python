#
# @lc app=leetcode id=825 lang=python3
#
# [825] Friends Of Appropriate Ages
#
from typing import List


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages_counter = [0 for i in range(121)]

        # 统计各年龄人数
        for i in range(len(ages)):
            ages_counter[ages[i]] += 1

        # 统计小于i年龄段人数的总和
        for i in range(1, 121):
            ages_counter[i] += ages_counter[i - 1]

        res = 0
        for i in range(len(ages)):
            # 根据公式计算出 a -> b 中 b 的取值区间
            low, high = int(0.5 * ages[i] + 7), int(ages[i])

            if low >= high:
                continue

            # 如果a也在区间中，说明重复计算了，需要减去
            if low < ages[i] <= high:
                res -= 1

            # 统计区间内的人数
            res += ages_counter[high] - ages_counter[low]

        return res


if __name__ == '__main__':
    print(Solution().numFriendRequests([16, 16]))
    print(Solution().numFriendRequests([16, 17, 18]))
    print(Solution().numFriendRequests([20, 30, 100, 110, 120]))
