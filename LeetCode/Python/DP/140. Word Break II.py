"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 140. Word Break II.py
@time: 18-12-23 下午2:13
@version: v1.0 
"""


class Solution(object):
    mem_cache = dict()

    def rec_wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        # if s in wordDict:
        #     self.mem_cache[s] = True
        #     return [s]

        if self.mem_cache.get(s, None) is not None:
            if not self.mem_cache[s]:
                return list()

        res_list = list()
        for i in range(len(s)):
            sub_a = s[:i]
            sub_b = s[i:]

            if sub_a == "" and sub_b in wordDict:
                self.mem_cache[sub_b] = True
                res_list.append(sub_b)
                continue

            if sub_a not in wordDict:
                continue

            self.mem_cache[sub_a] = True

            if sub_b in wordDict:
                self.mem_cache[sub_b] = True
                res_list.append(sub_a + " " + sub_b)

            sub_b_list = self.wordBreak(sub_b, wordDict)
            if sub_b_list:
                self.mem_cache[sub_b] = True
                res_list.extend([sub_a + " " + b for b in sub_b_list])
            else:
                self.mem_cache[sub_b] = False

        return sorted(list(set(res_list)))

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        mem = dict()

        def wordBreak(s):
            if s in mem:
                return mem[s]

            ans = list()
            if s in wordDict:
                ans.append(s)

            for i in range(1, len(s)):
                sub_a = s[:i]
                sub_b = s[i:]

                if sub_a not in wordDict:
                    continue

                ans.extend([sub_a + " " + b for b in wordBreak(sub_b)])

            mem[s] = ans
            return mem[s]

        return wordBreak(s)


if __name__ == '__main__':
    sol = Solution()
    print(sol.wordBreak(s="catsanddog", wordDict=["cat", "cats", "and", "sand", "dog"]))
    # print(sol.wordBreak(s="pineapplepenapple", wordDict=["apple", "pen", "applepen", "pine", "pineapple"]))
    print(sorted(sol.wordBreak("aaaaaaa", ["aaaa", "aa", "a"])))
    print(sol.wordBreak("a", ["a"]))
