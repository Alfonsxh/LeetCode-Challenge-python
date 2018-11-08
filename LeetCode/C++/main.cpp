//
// Created by alfons on 18-11-8.
//
#include <iostream>
#include <vector>

#include "Solution.h"

int main() {
    Solution sol;

    // 26. Remove Duplicates from Sorted Array
    std::vector<int> nums1{0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
    std::cout << "There have " << sol.removeDuplicates(nums1) << " diff elements." << std::endl;

    // 27. Remove Element
    std::vector<int> nums2{2, 2};
    std::cout << "There have " << sol.removeElement(nums2, 2) << " left elements." << std::endl;

    // 283. Move Zeroes
    std::vector<int> nums3{0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
    sol.moveZeroes(nums3);
    std::cout << "The new nums is " << nums3.data() << std::endl;

    // 80. Remove Duplicates from Sorted Array II
    std::vector<int> nums4{0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 5, 5, 5, 5, 5,};
    std::cout << "There have " << sol.removeDuplicates2(nums4) << " diff elements." << std::endl;

    return 1;
}