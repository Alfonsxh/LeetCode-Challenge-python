"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 139. Word Break.py
@time: 18-12-23 下午12:56
@version: v1.0 
"""


class Solution(object):
    mem_cache = dict()

    def rec_wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # if s in wordDict:
        #     return True

        if self.mem_cache.get(s, None) is not None:
            return self.mem_cache[s]

        for i in range(len(s)):
            sub_a = s[:i]
            sub_b = s[i:]

            if sub_a not in wordDict:
                continue

            if sub_b in wordDict:
                return True

            if self.rec_wordBreak(sub_b, wordDict):
                self.mem_cache[sub_b] = True
                return True
            else:
                self.mem_cache[sub_b] = False

        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.rec_wordBreak(s="applepenapple", wordDict=["apple", "pen"]))
    sol.mem_cache.clear()
    print(sol.rec_wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))
    sol.mem_cache.clear()
    print(sol.rec_wordBreak(s="leetcode", wordDict=["leet", "code"]))
    sol.mem_cache.clear()
    print(sol.rec_wordBreak(
        s="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
        wordDict=["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]))
