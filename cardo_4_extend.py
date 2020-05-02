
from pyeda.inter import exprvar
import itertools
import time

x4, x3, x2, notx1, x21, x22, notx21, notx22, x31, x32, notx31, notx32, x1, notx4 = map(exprvar, "x4 x3 x2 notx1 x21 x22 notx21 notx22 x31 x32 notx31 notx32 x1 notx4".split())
all_vars = [x1, notx1, x21, x22, notx21, notx22, x31, x32, notx31, notx32, x4, notx4]
equals = [(~x1, [notx1]), (x2,[x21, x22]), (~x2,[notx21, notx22]), (x3, [x31, x32]),(~x3, [notx31, notx32]), (~x4, [notx4])]
inputs = [x1, x2, x3, x4]
kardo_functions = {}
count = 0
i=0
start_time = time.time()


def calcFunction(function, i):
    #here is is point with dimension-size 4
    function=function.restrict({x4:i[3]})
    function = function.restrict({x3:i[2]})
    function = function.restrict({x2:i[1]})
    function = function.restrict({x1:i[0]})
    if function.satisfy_one() is not None:
        return 1
    return 0




def printFunction(function):
    res=[]
    #print(function)
    for i in list(itertools.product(range(2),repeat=4)):
        res.append(calcFunction(function,i))
    #print(str(res))
    return str(res)



for vec in list(itertools.product(range(3), repeat=12))[::-1]:
    i+=1
    d = dict(zip(all_vars, vec))
    function = ((notx1 & notx22 & notx32 & x4) |
    (notx1 & notx22 & x32 & notx4) |
    (notx1 & notx22 & notx32 & x31 & notx31 & notx4) |
    (notx1 & notx22 & x32 & notx31 & x31 & x4) |
    (x1 & x21 & notx32 & x4) |
    (x1 & x21 & x32 & notx4) |
    (x1 & x21 & notx32 & x31 & notx31 & notx4) |
    (x1 & x21 & x32 & notx31 & x31 & x4) |
    (x1 & notx21 & x22 & notx22 & notx32 & x4) |
    (x1 & notx21 & x22 & notx22 & x32 & notx4) |
    (x1 & notx21 & x22 & notx22 & notx32 & x31 & notx31 & notx4) |
    (x1 & notx21 & x22 & notx22 & x32 & notx31 & x31 & x4) |
    (notx1 & x22 & notx21 & x21 & notx32 & x4) |
    (notx1 & x22 & notx21 & x21 & x32 & notx4) |
    (notx1 & x22 & notx21 & x21 & notx32 & x31 & notx31 & notx4) |
    (notx1 & x22 & notx21 & x21 & x32 & notx31 & x31 & x4) |
    (x1 & notx21 & notx31 & notx4) |
    (x1 & notx21 & x31 & x4) |
    (x1 & notx21 & x31 & notx32 & x32 & notx4) |
    (x1 & notx21 & notx31 & x32 & notx32 & x4) |
    (notx1 & x22 & notx31 & notx4) |
    (notx1 & x22 & x31 & x4) |
    (notx1 & x22 & x31 & notx32 & x32 & notx4) |
    (notx1 & x22 & notx31 & x32 & notx32 & x4) |
    (notx1 & notx22 & x21 & notx21 & notx31 & notx4) |
    (notx1 & notx22 & x21 & notx21 & x31 & x4) |
    (notx1 & notx22 & x21 & notx21 & x31 & notx32 & x32 & notx4) |
    (notx1 & notx22 & x21 & notx21 & notx31 & x32 & notx32 & x4) |
    (x1 & x21 & notx22 & x22 & notx31 & notx4) |
    (x1 & x21 & notx22 & x22 & x31 & x4) |
    (x1 & x21 & notx22 & x22 & x31 & notx32 & x32 & notx4) |
    (x1 & x21 & notx22 & x22 & notx31 & x32 & notx32 & x4))
    if i%1000==0:
        print("# functions: ", i)
    restrict_dict = {key:value for key, value in d.items() if value in (0, 1)}
    #print(restrict_dict)
    function = function.restrict(restrict_dict)
   # print(function)
    for var, vars_lst in equals:
        for v in vars_lst:
            function = function.compose({v: var})
            #print(function)
            #print({v: var})
    fictitious_vars = [v for v in inputs]
    for v in fictitious_vars:
        function = function & (v | ~v)
    res=printFunction(function)
    if str(res) not in kardo_functions.keys():
        kardo_functions[str(res)]=restrict_dict


result=[]
for key,value in kardo_functions.items():
    result.append(str(key)+" : "+str(value))
with open("new_final_functions_extend.txt", "w") as f:
    f.write("\n".join(sorted(result)))

print("# functions: ", )
print("--- %s seconds ---" % (time.time() - start_time))
print(len(kardo_functions))