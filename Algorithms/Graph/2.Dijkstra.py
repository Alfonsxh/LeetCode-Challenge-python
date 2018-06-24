#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 2.Dijkstra.py
@time: 18-6-11 上午12:00
@version: v1.0 
"""
# 最短路径----狄克斯特拉
# 1.找到最短时间内能够到达的节点。
# 2.对于该节点的邻居节点，检查是否含有从起点通往他们更短的路径，如果有，就更新其开销。
# 3.重复这个过程，直到对每个节点都这样做。
# 4.计算最终的路径。

# 图
graph = dict()
graph["a"] = dict(b=7, c=9, d=14)
graph["b"] = dict(c=10, f=15)
graph["c"] = dict(f=11)
graph["d"] = dict(c=2, e=9)
graph["e"] = dict(f=6)

# 开销
infinity = float("inf")
costs = dict(b=7, c=9, d=14, e=infinity, f=infinity)

# 父节点
parents = dict(b="a", c="a", d="a", e=None, f=None)

# 处理节点标记列表
processed = list()


def FindLowestCostNode(costs):
    """
    查找当前未处理的节点中开销最小的节点
    :param costs: 开销列表
    :return: 开销最小的节点
    """
    lowestCost = infinity
    lowestCostNode = None

    for node in costs:
        cost = costs[node]
        if cost < lowestCost and node not in processed:
            lowestCost = costs[node]
            lowestCostNode = node
    return lowestCostNode


def Dijkstra():
    node = FindLowestCostNode(costs)       # 选择开销最小的节点
    while node:
        cost = costs[node]              # 最小节点开销
        neighbors = graph[node]         # 最小节点的邻居节点字典
        for n in neighbors.keys():          # 遍历最小节点的邻居节点
            newCast = cost + neighbors[n]   # 更新到邻居节点的开销
            if costs[n] > newCast:          # 如果旧的开销大于新的开销
                costs[n] = newCast          # 则更新新的开销
                parents[n] = node           # 并将父节点重新赋值
        processed.append(node)              # 处理列表新增处理后的节点
        node = FindLowestCostNode(costs)


if __name__ == "__main__":
    Dijkstra()
    pass
