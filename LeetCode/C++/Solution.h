//
// Created by alfons on 18-11-8.
//

#ifndef LEETCODE_SOLUTION_H
#define LEETCODE_SOLUTION_H

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        vector<int> tmpVec;

        auto L = nums.begin(), R = nums.begin();
        for (;  R != nums.end() ; R++) {
            if (*L != *R){
                tmpVec.push_back(*L);
                L =R;
            }
        }

        if (!nums.empty())
            tmpVec.push_back(*L);

        nums.swap(tmpVec);
        return (int)nums.size();
    }
};

#endif //LEETCODE_SOLUTION_H
