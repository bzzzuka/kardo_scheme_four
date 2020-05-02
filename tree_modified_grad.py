import copy
import random
import sys

import  itertools


class Point:
    def __init__(self, functions, visited):
        self.functions = functions
        self.visited = visited
        self.length=len(functions)

def choose_my_point(point,index):
    min_res = 2809
    vis=copy.deepcopy(point.visited)
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
    print(index)
    return Point(left_node,  vis), Point(right_node,  vis)

def calc(b,per):
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
    for i in levels:
        print()
    funcs=[]
    length=0
    visited=[]

    for i in levels[15]:
        if  i.length>length:
            length=i.length
            funcs=i.functions
            visited=i.visited
    return ("number of functions :"+str(length)+": "+str(funcs) + " visited points are:"+str(sorted(visited)))







# for b in range(30000):
#     if b%100==0:
#         print(b)
#     calc(b)

a=0
res=[]
for comb in itertools.combinations(range(0,16),4):
    res.append(str(calc(1,comb))+" for combination:" + str(comb))

    # if a%5==0 and a>0:
    #     print(a)
    #     print(res[a-1])
    if (a%50==0):
        print(a)
        print(res[a])
    a+= 1
with open("result_comb.txt", "w") as f:
    f.write("\n".join(res))
print(res)
