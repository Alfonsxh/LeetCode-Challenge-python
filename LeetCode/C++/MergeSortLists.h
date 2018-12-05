//
// Created by alfons on 18-12-5.
//

#ifndef LEETCODE_SORTLISTS_H
#define LEETCODE_SORTLISTS_H

using namespace std;

struct ListNode {
    int val;
    ListNode *next;

    ListNode(int x) : val(x), next(nullptr) {}
};

ListNode *CreateNodeList(int *input, int len) {
    ListNode *output = new ListNode(0);
    ListNode *head = output;

    for (int i = 0; i < len; ++i) {
        output->next = new ListNode(input[i]);
        output = output->next;
    }

    return head->next;
}

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

};

#endif //LEETCODE_SORTLISTS_H
