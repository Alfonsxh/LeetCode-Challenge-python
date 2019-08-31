#
# @lc app=leetcode id=950 lang=python3
#
# [950] Reveal Cards In Increasing Order
#
from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)

        res = list()
        for card in deck:
            if not res:
                res.append(card)
            else:
                p = res.pop()
                res.insert(0, p)
                res.insert(0, card)

        return res


if __name__ == '__main__':
    print(Solution().deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7]))
