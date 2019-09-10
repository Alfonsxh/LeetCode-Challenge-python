#
# @lc app=leetcode id=670 lang=python3
#
# [670] Maximum Swap
#
class Solution:
    def maximumSwap(self, num: int) -> int:
        num_list = list(str(num))
        res = num_list[:]

        # 主要思路是，替换各个位置上的数字，找到最大的一组，时间复杂度为 O(n^2)
        for i in range(len(num_list)):
            for j in range(1, len(num_list)):
                # 交换后的数字列表
                num_list[i], num_list[j] = num_list[j], num_list[i]

                # 判断数字列表的大小
                if num_list > res:
                    res = num_list[:]

                # 再次交换，复原列表，以免下一次调用发生错误
                num_list[i], num_list[j] = num_list[j], num_list[i]

        return int(''.join(res))

    # def maximumSwap(self, num: int) -> int:
    #     num_str = str(num)
    #     if len(num_str) == 1:
    #         return num
    #
    #     max_num = max(i for i in num_str)
    #     max_left_index = num_str.find(max_num)
    #     max_right_index = num_str.rfind(max_num)
    #
    #     if max_left_index == 0:
    #         next_num_str = num_str[1:]
    #         next_true_num_str = str(int(next_num_str))
    #         zero_num = len(next_num_str) - len(next_true_num_str)
    #         return int(num_str[0] + '0' * zero_num + str(self.maximumSwap(int(next_true_num_str))))
    #     else:
    #         num_list = [n for n in num_str]
    #         num_list[max_right_index], num_list[0] = num_list[0], num_list[max_right_index]
    #         return int(''.join(num_list))


if __name__ == '__main__':
    r = "2736".rfind('7')

    assert Solution().maximumSwap(99901) == 99910
    assert Solution().maximumSwap(100) == 100
    assert Solution().maximumSwap(1993) == 9913
    assert Solution().maximumSwap(10) == 10
    assert Solution().maximumSwap(2736) == 7236
    assert Solution().maximumSwap(9976) == 9976
    assert Solution().maximumSwap(98368) == 98863
