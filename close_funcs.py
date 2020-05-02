def find_close(f1,f2):
    count=0
    for i in range(16):
        if f1[i]!=f2[i]:
            count+=1
    return  count==1


functions = []
with open('new_final_functions.txt', 'r') as f:
    functions = [list(tuple([int(x) for x in line.strip()[1:-1].split(',')])) for line in f.readlines()]
levels=[[] for _ in range(17)]
functions_list=[]
for function in functions:
    count=function.count(1)
    levels[count].append(function)
res=dict()
for f in functions:
    level=f.count(1)
    count=0
    close=[]
    if level==0:
        check=[1]
    elif level==16:
        check==[15]
    else:
        check=[level-1,level+1]
    for i in check:
        for function in levels[i]:
            if find_close(f,function):
                close.append(function)
    if len(close)>=16:
        res[str(f)]=sorted(close)
print(res)
print(len(res))








