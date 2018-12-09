//
// Created by alfons on 18-12-5.
//

#ifndef LEETCODE_SORTLISTS_H
#define LEETCODE_SORTLISTS_H

#include <algorithm>
#include <vector>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;

    ListNode(int x) : val(x), next(nullptr) {}
};

/**
 * 根据输入的int数组创建对应的节点列表
 * @param input 输入数组指针
 * @param len 数组长度
 * @return 节点列表
 */
ListNode *CreateNodeList(int *input, int len) {
    ListNode *output = new ListNode(0);
    ListNode *head = output;

    for (int i = 0; i < len; ++i) {
        output->next = new ListNode(input[i]);
        output = output->next;
    }

    return head->next;
}

/**
 * 打印节点列表
 * @param nodeList 节点列表
 */
void PrintNodeList(ListNode *nodeList) {
    while (nodeList != nullptr) {
        cout << nodeList->val;
        nodeList = nodeList->next;
        if (nodeList != nullptr) {
            cout << " -> ";
        }
        std::flush(std::cout);
    }
    cout << endl;
    std::flush(std::cout);
}

class MergeSortLists {
public:
    // 21. Merge Two Sorted Lists
    ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) {
        ListNode *result = new ListNode(0);
        ListNode *head = result;

        while (l1 != nullptr && l2 != nullptr) {
            if (l1->val < l2->val) {
                result->next = l1;
                l1 = l1->next;
            } else {
                result->next = l2;
                l2 = l2->next;
            }
            result = result->next;
        }

        if (l1 == nullptr)
            result->next = l2;
        else
            result->next = l1;

        return head->next;
    }

    // 88. Merge Sorted Array
    void merge(vector<int> &nums1, int m, vector<int> &nums2, int n) {
        vector<int> tmp;

        int i = 0, j = 0;
        while (i < m && j < n) {
            if (nums1[i] < nums2[j]) {
                tmp.push_back(nums1[i]);
                ++i;
            } else {
                tmp.push_back(nums2[j]);
                ++j;
            }
        }

        if (i == m) {
            while (j < n) {
                tmp.push_back(nums2[j]);
                ++j;
            }
        } else {
            while (i < m) {
                tmp.push_back(nums1[i]);
                ++i;
            }
        }

        nums1.swap(tmp);
    }

    // 23. Merge k Sorted Lists
    static bool Comper(ListNode *node1, ListNode *node2) {
        return node1->val > node2->val;
    }

    ListNode *mergeKLists(vector<ListNode *> &lists) {
        // 初始化堆
        std::vector<ListNode *> node_heap;
        node_heap.reserve(lists.size());
        for (auto node: lists) {
            if (node) node_heap.push_back(node);
        }

        if (node_heap.empty())
            return nullptr;

        std::make_heap(node_heap.begin(), node_heap.end(), Comper);

        // 循环读取最小值，并补充元素
        ListNode *result = new ListNode(0);
        ListNode *head = result;
        while (!node_heap.empty()) {
            // 获取最小值，并从堆中剔除它
            std::pop_heap(node_heap.begin(), node_heap.end(), Comper);
            ListNode *min_node = node_heap.back();
            node_heap.pop_back();

            // 存储最小值
            result->next = min_node;
            result = result->next;

            // 将最小元素的下一个元素入堆
            if (min_node->next) node_heap.push_back(min_node->next);
            std::push_heap(node_heap.begin(), node_heap.end(), Comper);
        }

        return head->next;
    }

};

#endif //LEETCODE_SORTLISTS_H
