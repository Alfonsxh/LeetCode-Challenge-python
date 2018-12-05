cmake_minimum_required(VERSION 3.0)
project(LeetCode)

# 设置c++11 选项
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

add_executable(LeetCodeCPlusPlus main.cpp NotRepeatElement.h MergeSortLists.h BaseFunc.h)