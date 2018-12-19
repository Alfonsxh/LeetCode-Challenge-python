"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 746. Min Cost Climbing Stairs.py
@time: 18-12-19 下午9:57
@version: v1.0 
"""


class Solution(object):
    def rec_minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) < 2:
            return 0

        return min(self.rec_minCostClimbingStairs(cost[:-1]) + cost[-1],
                   self.rec_minCostClimbingStairs(cost[:-2]) + cost[-2])

    def dp_minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) < 2:
            return 0

        a = cost[0]
        b = cost[1]

        for i in range(len(cost) - 2):
            tmp = min(b, a) + cost[i + 2]
            a = b
            b = tmp

        return min(a, b)


if __name__ == '__main__':
    sol = Solution()
    print(sol.rec_minCostClimbingStairs([0, 0, 0, 1]))
    print(sol.dp_minCostClimbingStairs([0, 0, 0, 1]))

    print(sol.rec_minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
    print(sol.dp_minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
