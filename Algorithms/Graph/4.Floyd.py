#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 4.Floyd.py
@time: 18-6-18 下午10:41
@version: v1.0 
"""

# 弗洛伊德算法

# 设  $D_{i,j,k}$为从$i$到$j$的只以 $(1..k)$集合中的节点为中间节点的最短路径的长度。
#
# - 若最短路径经过点k，则 $D_{i,j,k} = D_{i,k,k-1} + D_{k,j,k-1}$；
# - 若最短路径不经过点k，则 $D_{i,j,k}=D_{i,j,k-1}$。
#
# 因此， $D_{i,j,k}=min(D_{i,j,k-1},D_{i,k,k-1}+D_{k,j,k-1})$。

# 图
infinity = float("inf")
graph = dict()
graph["a"] = dict(a=0, b=2, c=6, d=4)
graph["b"] = dict(a=infinity, b=0, c=3, d=infinity)
graph["c"] = dict(a=7, b=infinity, c=0, d=1)
graph["d"] = dict(a=5, b=infinity, c=12, d=0)


def Floyd():
    for k in graph.keys():              # 经过的第K个点
        for i in graph.keys():
            for j in graph.keys():
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]


if __name__ == "__main__":
    for i in graph.keys():
        print('    ,'.join(str(i) for i in list(graph[i].values())))
    print('\n\n')
    Floyd()
    for i in graph.keys():
        print('    ,'.join(str(i) for i in list(graph[i].values())))

    pass
