//
// Created by alfons on 18-11-8.
//
#include <iostream>
#include <vector>

#include "BaseFunc.h"

#include "NotRepeatElement.h"
#include "MergeSortLists.h"

int main() {

    // ----------------------元素去重leetcode--------------------------
    NotRepeatElement notRepeatElement;

    // 26. Remove Duplicates from Sorted Array
    std::vector<int> nums1{0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
    std::cout << "There have " << notRepeatElement.removeDuplicates(nums1) << " diff elements." << std::endl;

    // 27. Remove Element
    std::vector<int> nums2{2, 2};
    std::cout << "There have " << notRepeatElement.removeElement(nums2, 2) << " left elements." << std::endl;

    // 283. Move Zeroes
    std::vector<int> nums3{0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
    notRepeatElement.moveZeroes(nums3);
    std::cout << "The new nums is " << nums3.data() << std::endl;

    // 80. Remove Duplicates from Sorted Array II
    std::vector<int> nums4{0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 5, 5, 5, 5, 5,};
    std::cout << "There have " << notRepeatElement.removeDuplicates2(nums4) << " diff elements." << std::endl;

    // -----------------------归并排序---------------------------------
    MergeSortLists MegreSort;

    // 21. Merge Two Sorted Lists
    int l1[] = {1, 2, 4, 5, 6, 8};
    int l2[] = {1, 3, 4};
    ListNode *node_list_1 = CreateNodeList(l1, sizeof(l1) / sizeof(l1[0]));
    ListNode *node_list_2 = CreateNodeList(l2, sizeof(l2) / sizeof(l2[0]));

    PrintNodeList(MegreSort.mergeTwoLists(node_list_1, node_list_2));

    // 88. Merge Sorted Array
    vector<int> vec_l1 = {1, 2, 3, 0, 0, 0};
    vector<int> vec_l2 = {2, 5, 6};

    MegreSort.merge(vec_l1, 3, vec_l2, 3);
    PrintIterator(vec_l1);
    return 1;
}