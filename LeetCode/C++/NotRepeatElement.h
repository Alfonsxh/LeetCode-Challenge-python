//
// Created by alfons on 18-11-8.
//

#ifndef LEETCODE_SOLUTION_H
#define LEETCODE_SOLUTION_H

#include <iostream>
#include <vector>

using namespace std;

class NotRepeatElement {
public:
    // 26. Remove Duplicates from Sorted Array
    int removeDuplicates(vector<int> &nums) {
        vector<int> tmpVec;

        auto L = nums.begin(), R = nums.begin();
        for (; R != nums.end(); R++) {
            if (*L != *R) {
                tmpVec.push_back(*L);
                L = R;
            }
        }

        if (!nums.empty())
            tmpVec.push_back(*L);

        nums.swap(tmpVec);
        return (int) nums.size();
    }

    // 80. Remove Duplicates from Sorted Array II
    int removeDuplicates2(vector<int> &nums) {
        vector<int> tmpVec;

        int L = 0, R = 0;
        for (; R < nums.size(); R++) {
            if (nums[L] == nums[R] && R - L < 2) {
                tmpVec.push_back(nums[L]);
            }

            if (nums[L] != nums[R]) {
                tmpVec.push_back(nums[R]);
                L = R;
            }

        }

        nums.swap(tmpVec);
        return (int) nums.size();
    }

    // 27. Remove Element
    int removeElement(vector<int> &nums, int val) {
        vector<int> tmpVec;

        for (auto n : nums) {
            if (n != val) {
                tmpVec.push_back(n);
            }
        }

        nums.swap(tmpVec);
        return nums.size();
    }

    // 283. Move Zeroes
    void moveZeroes(vector<int> &nums) {
        int L = 0;

        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] != 0) {
                swap(nums[L++], nums[i]);
            }
        }
    }
};

#endif //LEETCODE_SOLUTION_H
