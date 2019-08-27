#
# @lc app=leetcode id=1013 lang=python3
#
# [1013] Partition Array Into Three Parts With Equal Sum
#
from typing import List


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total_sum = sum(A)
        if total_sum % 3 != 0:
            return False

        part_sum = total_sum // 3
        part_num = 0
        tmp_sum = part_sum
        for i in range(len(A)):
            if tmp_sum - A[i] == 0:
                tmp_sum = part_sum
                part_num += 1
            else:
                tmp_sum -= A[i]

            if part_num == 2:       # 只需要判断两个分区即可
                return True

        return False


if __name__ == '__main__':
    print(Solution().canThreePartsEqualSum([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]))        # False
    print(Solution().canThreePartsEqualSum([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]))        # True
