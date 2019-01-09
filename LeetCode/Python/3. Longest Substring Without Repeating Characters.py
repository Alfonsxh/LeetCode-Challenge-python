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
        :type s: str
        :rtype: int
        """
        start = maxLength = 0
        usedChart = dict()

        for index in range(len(s)):
            # 如果当前字符不在使用的字符中，或者开始统计的位置在已使用字符索引之后，计算最大长度
            if s[index] not in usedChart.keys() or start > usedChart[s[index]]:
                maxLength = max(maxLength, index - start + 1)
            else:
                start = usedChart[s[index]] + 1

            usedChart.update({s[index]: index})

        return maxLength


if __name__ == '__main__':
    sol = Solution()
    # print(sol.lengthOfLongestSubstring("abcabcbb"))
    # print(sol.lengthOfLongestSubstring("bbbb"))
    # print(sol.lengthOfLongestSubstring("pwwkew"))
    print(sol.lengthOfLongestSubstring("tmmzuxt"))
