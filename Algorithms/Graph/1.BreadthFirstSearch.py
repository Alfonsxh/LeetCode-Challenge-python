#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 1.BreadthFirstSearch.py
@time: 18-6-10 下午11:57
@version: v1.0 
"""

# 广度优先搜索
# 步骤：
# 1、首先将根节点放入队列中。
# 2、从队列中取出第一个节点，并检验它是否为目标。
#    如果找到目标，则结束搜索并回传结果。
#    否则将它所有尚未检验过的直接子节点加入队列中。
# 3、若队列为空，表示整张图都检查过了——亦即图中没有欲搜索的目标。结束搜索并回传“找不到目标”。
# 4、重复步骤2。

from queue import Queue
from Algorithms.LogDecorator import PrintfDecorator

# 例子，从关系表中，通过广度优先搜索出目标联系人
graph = dict()
graph["You"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def AndSearchTarget(targetQueue, targetList):
    for target in targetList:
        targetQueue.put(target)


@PrintfDecorator
def FindPerson(firsonPerson, targetPerson):
    searchQueue = Queue()
    AndSearchTarget(searchQueue, graph[firsonPerson])

    parseList = list()

    while not searchQueue.empty():
        target = searchQueue.get()
        if target in parseList:
            continue

        if target == targetPerson:
            print("It's target persion {target}!".format(target=targetPerson))
            return True

        AndSearchTarget(searchQueue, graph[target])
        parseList.append(target)
    return False


# 深度优先
DBFParseList = list()


def FindPerson2(firsonPerson, targetPerson):
    for target in graph[firsonPerson]:
        if target in DBFParseList:
            continue

        if target == targetPerson:
            print("It's target persion {target}!".format(target=targetPerson))
            return True

        if FindPerson2(target, targetPerson):
            return True


if __name__ == "__main__":
    FindPerson("You", "jonny")
    FindPerson2("You", "jonny")
