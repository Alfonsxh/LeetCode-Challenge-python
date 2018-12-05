//
// Created by alfons on 18-12-5.
//

#ifndef LEETCODE_BASEFUNC_H
#define LEETCODE_BASEFUNC_H

#include <iostream>

template<typename T>
void PrintIterator(T &iterObj) {
    for (auto i : iterObj) {
        std::cout << i << " ";
        std::flush(std::cout);
    }
}

#endif //LEETCODE_BASEFUNC_H
