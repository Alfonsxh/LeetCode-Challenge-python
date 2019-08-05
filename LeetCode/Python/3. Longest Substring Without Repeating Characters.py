"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 3. Longest Substring Without Repeating Characters.py
@time: 19-1-9 下午9:34
@version: v1.0 
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        大意是查找目标字符串中的无重复字符的最长子字符串。

        问题的关键点在于，遇到重复字符时的处理。

        从头开始遍历整个目标字符串，将无重复子串的开头索引设置为start，则无重复子串的长度为当前位置的索引index - start + 1.

        并且设置单个字符最近一次出现的索引字典为 usedCharDict = {c : last_index}

        当遍历目标字符串时，如果（字符不在已使用的字符中） 或者 （字符在已使用的字符中，start 的位置 大于已使用的字符的最后一次索引）
        ，则最大的长度为保存的最大长度 maxLength 与 index - start + 1 中的最大值。

        否则，将开始位置 start 置为遍历的字符最近一次出现的索引位置的后一个位置。

        :type s: str
        :rtype: int
        """
        start = maxLength = 0
        usedCharDict = dict()

        for index in range(len(s)):
            # 如果当前字符不在使用的字符中，或者开始统计的位置在已使用字符索引之后，计算最大长度
            if s[index] not in usedCharDict.keys() or start > usedCharDict[s[index]]:
                maxLength = max(maxLength, index - start + 1)
            else:
                start = usedCharDict[s[index]] + 1

            usedCharDict.update({s[index]: index})

        return maxLength


if __name__ == '__main__':
    sol = Solution()
    # print(sol.lengthOfLongestSubstring("abcabcbb"))
    # print(sol.lengthOfLongestSubstring("bbbb"))
    # print(sol.lengthOfLongestSubstring("pwwkew"))
    print(sol.lengthOfLongestSubstring("tmmzuxt"))
