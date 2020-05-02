import copy
import random
import sys

import  itertools


class Point:
    def __init__(self, functions, visited):
        self.functions = functions
        self.visited = visited
        self.length=len(functions)


def choose_best_point(point):
    min_res = 2809
    vis=copy.deepcopy(point.visited)
    index = -1
    for i in range(0,16):
        count_1 = 0
        count_0 = 0
        if i in vis:
            continue
        for func in point.functions:
            if func[i] == 1:
                count_1 += 1
            else:
                count_0 += 1
        if abs(count_1 - count_0) < min_res:
            min_res = abs(count_1 - count_0)
            index = i
    left_node = []
    right_node = []
    for func in point.functions:
        if func[index] == 1:
            left_node.append(func)
        else:
            right_node.append(func)
    if index == -1:
        return [], []
    vis.append(index)
    return Point(left_node,  vis), Point(right_node,  vis)

sys.setrecursionlimit(100000)
functions = []
with open('new_final_functions.txt', 'r') as f:
    functions = [tuple([int(x) for x in line.strip()[1:-1].split(',')]) for line in f.readlines()]
start_point = [Point(functions, [])]
levels = [start_point]


for i in range(1, 16):
    level = []
       # print(i)
        #print(levels[i-1])
    for point in levels[i - 1]:
            #if i<6:
            # left, right = choose_my_point(point,per[i-1])
            #else:
        left, right = choose_best_point(point)
        level.append(left)
        level.append(right)

    levels.append(level)
for i in levels[-1]:
    print(i.functions)

