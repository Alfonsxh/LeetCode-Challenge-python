//
// Created by alfons on 18-11-8.
//
#include <iostream>
#include <vector>

#include "Solution.h"

int main() {
    Solution sol;

    // 26. Remove Duplicates from Sorted Array
    std::vector<int> nums{0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
    std::cout << "There have " << sol.removeDuplicates(nums) << " diff elements." << std::endl;

    return 1;
}