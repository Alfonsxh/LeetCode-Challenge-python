#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = list()
        candidates.sort()
        self.__search(candidates, [], target)

        return self.res

    def __search(self, candidates, digits, target):
        # 唯一终止条件，digits中的所有元素之和等于target时终止
        if sum(digits) == target:
            self.res.append(digits)
            return

        for i in range(len(candidates)):
            # 此处为的是去除重复的元素
            # 如[1,1,2,5,6,7,10],前两个元素得去除
            # 但是，[1,2,5,6,7,10] 递归中的不用去除，第一个元素已经被取出，存在了digits中
            if i > 0 and candidates[i] == candidates[i-1]:
                continue

            if sum(digits) + candidates[i] <= target:
                self.__search(candidates[i+1:], digits + [candidates[i]], target)


if __name__ == '__main__':
    print(Solution().combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))
