#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 3.BellmanFord.py
@time: 18-6-18 下午4:55
@version: v1.0 
"""
# 最短路径----贝尔曼弗洛德算法
# for i in |V-1|:
#   if d(A->U) + d(U->V) < d(A->V):
#       d(A->V) = d(A->U) + d(U->V)

from collections import namedtuple

# 图
graph = dict()
graph["D"] = dict(B=1, C=5)
graph["B"] = dict(C=3, D=2, E=2)
graph["A"] = dict(B=-1, C=4)
graph["E"] = dict(D=-3)

# 开销
infinity = float("inf")
costs = dict(A=0, B=infinity, C=infinity, D=infinity, E=infinity)

# 父节点
parents = dict()

EdgeType = namedtuple("edge", "U,V,len")


def BellmanFord():
    # 构造边集合
    edgeList = list()
    for U, value in graph.items():
        for V, length in value.items():
            edgeList.append(EdgeType(U=U, V=V, len=length))

    # 算法主体
    for i in range(len(graph.keys()) - 1):                      # 遍历顶点数-1次
        for edge in edgeList:                                   # 遍历的所有的边集合
            if costs[edge.U] + edge.len < costs[edge.V]:        # relaxa(松弛主体)
                costs[edge.V] = costs[edge.U] + edge.len
                parents[edge.V] = edge.U

    # 回环判断
    for edge in edgeList:
        if costs[edge.U] + edge.len < costs[edge.V]:
            return True
    return False


if __name__ == "__main__":
    print("It's have loopback？\n{answer}".format(answer="Yes!" if BellmanFord() else "No!"))
